#coding: utf-8

__all__ = ['op']


import re

_ = re.compile(u'^(打开|关闭)(.*)')


def op(c):
    ret = _.findall(c)
    if ret:
        operation, obj = ret[0]
        return operation, obj.strip()
    return None, None
