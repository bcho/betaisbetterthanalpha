#coding: utf-8

__all__ = ['op']

import sqlite3

from front import config


connection = sqlite3.connect(config.DB_PATH)


def op(op, obj):
    return connection
