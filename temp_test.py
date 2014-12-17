# coding: utf8
__author__ = 'JinXing'


class ODict(object):
    def __init__(self, dict_=None, **kwargs):
        self.dict = {}
        if dict_:
            assert isinstance(dict_, dict)
            self.dict = dict_
        if kwargs:
            self.dict.update(kwargs)

    def __getattr__(self, attr):
        return self.dict[attr]


o = ODict({"name": 1}, value=10)
print o.name
print o.value
