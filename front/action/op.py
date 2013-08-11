#coding: utf-8

__all__ = ['op']

import sqlite3

from front import config


def op(op, obj):
    connection = sqlite3.connect(config.DB_PATH)
    cursor = connection.cursor()

    if op == u'关闭':
        op = 'close'
    elif op == u'打开':
        op = 'open'

    if obj == u'电视':
        obj = 'tv'
    elif obj == u'空调':
        obj = 'air'
    elif obj == 'ir':
        obj = 'ir'
    else:
        return False

    value = '%s:%s' % (op, obj)

    cursor.execute('''INSERT INTO `jobs` (`value`)
            VALUES(:value)''', {'value': value})

    connection.commit()

    return True
