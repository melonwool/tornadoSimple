#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys
import os
import time
import pymongo
import tornado

from tornado.options import define, options
from os.path import dirname, join, abspath

SRC_ROOT = dirname(abspath(__file__))
APP_ROOT = dirname(SRC_ROOT)

if APP_ROOT not in sys.path:
    sys.path.append(APP_ROOT)


import service
from utils import load_config

default_log_file_prefix = join(APP_ROOT, 'log')
define("debug", default=False, help="Debug Mode", type=bool)
define("port", default=8000, help="default:8000, required runserver", type=int)

def setup():
    config = load_config(APP_ROOT, 'config')

if __name__ == '__main__':
    reload(sys)
    sys.setdefaultencoding("UTF-8")
    
    tornado.options.parse_command_line()
    if options.debug:
        options.logging = 'debug'

    setup()

    #启动 tornado http server
    #logging.info("[httpd] start, port:%s, debug:%s, logging:%s", options,port, options.debug, options.logging)
    app = service.Application(debug = options.debug)
    app.setup(APP_ROOT)

    http_server = tornado.httpserver.HTTPServer(app, xheaders=True)
    http_server.listen(options.port)
    tornado.ioloop.IOLoop.instance().start()
