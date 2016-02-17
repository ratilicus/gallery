#!ve/bin/python

'''
Gallery Server
by: Adam Dybczak (RaTilicus)
'''

import time
import tornado.web, tornado.ioloop
from tornado import gen
from handlers import IndexHandler, UploadHandler


if __name__ == '__main__':
    print 'INIT'

    SETTINGS = {
        't': int(time.time()),
        'cookie_secret': "__TODO:_GENERATE_YOUR_OWN_RANDOM_VALUE_HERE__",
        "login_url": "/login",
        #'xsrf_cookies': True,
        'autoreload': True,
        'debug': True,
        'STATIC_PATH': 'static',
    }

    try:
        # update settings based on secrets file (not to be shared with github)
        import __secrets__ as secret
        SETTINGS.update(secret.SETTINGS)
    except:
        pass

    URLS = (
        (r"^/$", IndexHandler),
        (r"^/upload/$", UploadHandler),
        (r'^/static/(.*)', tornado.web.StaticFileHandler, {'path': SETTINGS['STATIC_PATH']}),
    )

    application = tornado.web.Application(URLS, **SETTINGS)
    application.listen(8000)
    print 'START'
    tornado.ioloop.IOLoop.instance().start()
    
    print 'END'

