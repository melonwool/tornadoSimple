#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import os
import logging
import tornado.httpserver
import tornado.web
import tornado.netutil

from os.path import dirname, join, abspath

import redis
import pymongo

#from lib import torndb

from handlers import *

from utils import load_config
from models import MGModel

__version__ = '0.3.6'

#版本信息
class VersionHandler(tornado.web.RequestHandler):
    def get(self):
        self.finish("v" + __version__)


#
class Application(tornado.web.Application):
    def __init__(self, debug = False):
        handlers = [
            (r"/", IndexHandler),
            (r"/admin/login", AdminLoginHandler),
            (r"/version", VersionHandler),
        ]

        settings = dict(
            debug = debug,
            template_path = join(dirname(__file__), "templates"),
            static_path = join(dirname(__file__), "static"),
            gzip = False,
        )

        tornado.web.Application.__init__(self, handlers, **settings)

    def setup(self, root):
        """初始化数据"""
        self.app_root = root
        self.config = load_config(root, 'config')

        self._setup_mongo()
        #self._setup_redis()

        #MGModel.setup(self.mongo, cache = self.cache)
        MGModel.setup(self.mongo)

        return
    
    def _setup_mongo(self):
        cfg = self.config['mongo']
        self.mongo = pymongo.Connection(
                host = cfg['host'],
                port = int(cfg.get('port', 27017)),
                network_timeout = cfg.get('timeout', None),
                tz_aware = True
            )
        return
    def _setup_redis(self):
        cache = None
        cfg = self.config.get('redis', None)
        self.cache = redis.StrictRedis(
            host = cfg['host'],
            port = int(cfg.get('port', 6379)),
            db = int(cfg.get('db', 0)),
            password = cfg.get('pass',None)
            )
        return
