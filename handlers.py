'''
Gallery Tornado Server View Handlers
by: Adam Dybczak (RaTilicus)
'''

import tornado.web
from json import loads as json_decode, dumps as json_encode
from tornado import gen
from base64 import b64decode
from bson import ObjectId


class P(dict):
    def get(self, name, default=None):
        return super(P, self).get(name)[0] if name in self else default

    def pop(self, name, default=None):
        return super(P, self).pop(name, default)[0] if name in self else default

    def dict(self):
        return {k: v[0] for k,v in super(P, self).items()}



class BaseHandler(tornado.web.RequestHandler):
    @gen.coroutine
    def prepare(self):
        ''' handler init
        - set self.POST from request body, decode json if request is json
        '''
        self.POST = {}
        if self.request.method in ['POST', 'PUT'] and self.request.body:
            try:
                self.POST = P(json_decode(self.request.body))
            except Exception, e:
                self.POST = P(self.request.arguments)

    @gen.coroutine
    def render(self, template, **data):
        ''' render template override
        adds extra common template variables
        '''
        data['t'] = self.settings['t']
        super(BaseHandler, self).render(template, **data)

    @gen.coroutine
    def json_response(self, data, success=False, errors=[]):
        ''' json response helper '''
        self.write(json_encode({
            'data': data,
            'success': success,
            'errors': errors
        }))
        self.finish()


class IndexHandler(BaseHandler):
    @gen.coroutine
    def get(self):
        data = {}
        self.render('templates/index.html', **data)

class DataHandler(BaseHandler):
    @gen.coroutine
    def get(self):
        data = {}
        self.json_response(data, success=True)

#ref: http://stackoverflow.com/questions/11909397/how-to-upload-an-image-with-python-tornado-from-an-html-form
class UploadHandler(BaseHandler):
    @gen.coroutine
    def post(self):
        _id = self.POST.get('id', None)
        size = self.POST.get('size', 'full')
        header, binary_data = self.POST.pop('data').split(',', 1)
        print self.POST.dict(), len(binary_data)
        file_data = b64decode(binary_data)
        _id = ObjectId(_id)
        with open('uploads/{}_{}.jpg'.format(_id, size), 'wb') as of:
            of.write(file_data)
        
        data={'id': str(_id)}
        self.json_response(data, success=True)


