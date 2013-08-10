#coding: utf-8

__all__ = ['op', 'op_failed']


def op(operation, obj):
    return u'已经成功%s%s了' % (operation, obj)


def op_failed(operation, obj):
    return u'%s%s失败了 QAQ' % (operation, obj)
