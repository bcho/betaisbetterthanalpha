#coding: utf-8

__all__ = ['get_report']

import sqlite3

from front import config


def get_report():

    def _decorate(row):
        if not row:
            return {}
        return {
            'id': row[0],
            'value': row[1]
        }

    connection = sqlite3.connect(config.DB_PATH)
    cursor = connection.cursor()

    cursor.execute('''SELECT * FROM `stats`
        WHERE `consumed` = 0
        ORDER BY `created` DESC LIMIT 1;''')

    ret = _decorate(cursor.fetchone())

    return u'值: %s' % ret['value']
