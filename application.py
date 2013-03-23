#from tornado.wsgi import WSGIContainer
#from tornado.httpserver import HTTPServer
#from tornado.ioloop import IOLoop

from app.helpers.middleware import app

from app.helpers.errorhandler import *
import config.routing

#http_server = HTTPServer(WSGIContainer(app))
#http_server.listen(5000)
#IOLoop.instance().start()

if __name__ == '__main__':
    app.run()
