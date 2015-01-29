# -*- coding: utf-8 -*-
import tornado.web
import models import MGMessage

class AdminLoginHandler(tornado.web.RequestHandler):
    def get(self):
        self.render('admin/login.html')
    def post(self):
        pass
