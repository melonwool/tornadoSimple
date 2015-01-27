# -*- coding: utf-8 -*-
import tornado.web
from models import MGMessage

class IndexHandler(tornado.web.RequestHandler):
    def get(self):
        messages = MGMessage().getMessages()
        self.render('index.html', TITLE='留言板', messages=messages)
    
    def post(self):
        name = self.get_argument('name')
        says = self.get_argument('says')
        MGMessage().addMessage(name, says)
        self.redirect('/')
