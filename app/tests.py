#!ve/bin/python


"""
Gallery Tornado Server Tests
by: Adam Dybczak (RaTilicus)
"""


import unittest
from tornado.testing import AsyncHTTPTestCase
import motor
import pymongo
from bson import ObjectId
import web
import os
import shutil
from json import loads as json_decode


class TestWebApp(AsyncHTTPTestCase):
    def get_app(self):
        self.db = motor.MotorClient(host='db').test_gallery
        self.sync_db = pymongo.MongoClient(host='db').test_gallery
        self.UPLOAD_PATH = '/data/test_uploads/'
        if os._exists(self.UPLOAD_PATH):
            print 'UPLOAD PATH {} exists.. removing'.format(self.UPLOAD_PATH)
            shutil.rmtree(self.UPLOAD_PATH)

        self.settings = web.SETTINGS
        self.settings.update(autoreload=False, UPLOAD_PATH=self.UPLOAD_PATH, db=self.db)
        self.app = web.make_app(self.settings)
        return self.app

    def test_image_list_empty(self):
        self.sync_db.img.drop()
        response = self.fetch('/image/')

        self.assertEqual(response.code, 200)
        self.assertEqual(response.body, '{"errors": [], "data": {"objs": []}, "success": true}')

    def test_image_list(self):
        self.sync_db.img.drop()

        r1 = self.sync_db.img.insert({'fs': 1000})
        r2 = self.sync_db.img.insert({'fs': 1001, 'pid': 1000})
        r3 = self.sync_db.img.insert({'fs': 1002})
        r4 = self.sync_db.img.insert({'fs': 1003, 'pid': 1002})

        response = self.fetch('/image/')
        self.assertEqual(response.code, 200)
        json = json_decode(response.body)
        self.assertItemsEqual(json['data']['objs'], [
            {'_id': str(r2), 'pid': '1000', 'fs': 1001},
            {'_id': str(r4), 'pid': '1002', 'fs': 1003}
        ])

    def test_upload_image(self):
        self.sync_db.img.drop()
        body = 'data=,dGVzdCBkYXRh'
        response = self.fetch('/upload/', method='POST', body=body)
        self.assertEqual(response.code, 200)
        json = json_decode(response.body)
        _id = ObjectId(json['data']['id'])
        self.assertEqual(self.sync_db.img.count(), 1)
        obj = self.sync_db.img.find_one({'_id': _id})
        self.assertEqual(obj['fs'], 12)
        self.assertEqual(obj['pid'], None)
        file_data = open('{}/{}.jpg'.format(self.settings['UPLOAD_PATH'], _id), 'rb').read()
        self.assertEqual(file_data, 'test data')

    def test_upload_image_w_pid(self):
        self.sync_db.img.drop()
        body = 'data=,dGVzdCBkYXRhIGFnYWlu&id=5781d84e2fe7e60000000000'
        response = self.fetch('/upload/', method='POST', body=body)
        self.assertEqual(response.code, 200)
        json = json_decode(response.body)
        _id = ObjectId(json['data']['id'])
        self.assertEqual(self.sync_db.img.count(), 1)
        obj = self.sync_db.img.find_one({'_id': _id})
        self.assertEqual(obj['fs'], 20)
        self.assertEqual(obj['pid'], ObjectId('5781d84e2fe7e60000000000'))
        file_data = open('{}/{}.jpg'.format(self.settings['UPLOAD_PATH'], _id), 'rb').read()
        self.assertEqual(file_data, 'test data again')

    def test_get_image(self):
        pass


if __name__ == '__main__':
    unittest.main()
