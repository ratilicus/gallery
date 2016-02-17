'''
7D2D map markers Tornado Server
by: Adam Dybczak (RaTilicus)

user: [{
    _id: objectid,
    username: str,
    name: str,
    password: str,
    admin: bool
},]

source_image: [{
    _id: objectid,
    uploader: user._id
    editors: [user._id,],
    approval: {user._id: {status: int, reason: str},},  # approval status: 1:approve, 0:abstain, -1:deny
    alt: str, 
    desc: str, 
    width: int, 
    height: int,
    filename: str,
    catalogs: [
        {image_id: objectid, catalog_id: catalog._id, center: [int, int], scale: float, rotation: int},
    ],
    created: datetime,
},]

catalog: {
    _id: objectid,
    title: str,
    description: str,
    editors: [user._id,],
    viewers: [user._id,],
    approval: {user._id: {status: int, reason: str},},  # approval status: 1:approve, 0:abstain, -1:deny
    public: bool
    images: [
        {_id: objectid, source: source_image._id, filename: str, width: int, height: int, 
         cellx: int, celly: int, cellw:int, cellh: int, approved: bool},
    ]
    created: datetime,
}

comment: [{
    _id: objectid,
    catalog: catalog._id,
    image: catalog.images._id
    owner: 


- upload/delete images
- re-arrange images
- scale/crop/rotate images
- catalogs add/modify/remove    (title: str, desc: str, editors: [], viewers: [], images: [])
- comments 


'''

import tornado.web
from json import loads as json_decode, dumps as json_encode
from tornado import gen
from base64 import b64decode


class P(dict):
    def get(self, name, default=None):
        return super(P, self).get(name, default)[0]

    def pop(self, name, default=None):
        return super(P, self).pop(name, default)[0]

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
        size = self.POST.get('size', 'full')
        header, binary_data = self.POST.pop('data').split(',', 1)
        print self.POST.dict(), len(binary_data)
        file_data = b64decode(binary_data)
        with open('uploads/out_{}.jpg'.format(size), 'wb') as of:
            of.write(file_data)
        
        data={}
        self.json_response(self, data, success=True)


