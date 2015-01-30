# -*- coding: utf-8 -*-
class MGModel(object):

    _mongo = None
    #_cache = None

    @classmethod
    def setup(cls, mongo, cache = None):
        cls._mongo = mongo
        #cls._cache = cache

    @property
    def db_message(self):
        return self._mongo.message
    @property
    def db_user(self):
        return self._mongo.message
