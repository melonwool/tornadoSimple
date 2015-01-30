# -*- coding: utf-8 -*-
from .common import MGModel
class MGMessage(MGModel):
    @property
    def db(self):
        return self.db_message

    def addMessage(self, name, says):
        message = {
            "name" :name,
            "says" :says
        }
        self.db.info.insert(message)

    def getMessages(self):
        messages = []
        for message in self.db.info.find():
            messages.append(message)
        return messages

class User(MGModel):
    @property
    def db(self):
        return self.db_user

    def findUser(self, name):
        where = {
            "name":name
        }
        return self.db.user.find_one(where)
    
