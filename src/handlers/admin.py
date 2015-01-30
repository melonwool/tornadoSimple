# -*- coding: utf-8 -*-
import tornado.web
from models import User
import hashlib
class AdminLoginHandler(tornado.web.RequestHandler):
    def get(self):
        self.render('admin/login.html')
    def post(self):
        username = self.get_argument('username')
        password = self.get_argument('password')
        if username and password:
            result = User().findUser(username)
            if result:
                if hashlib.md5(password).hexdigest() == result[u'password']:
                    self.write('ok')
                    #self.redirect('admin/index.html')
                else:
                    self.write('no equal')
        else:
            self.write('no')
