#coding: utf-8

__all__ = ['get_report']

import sqlite3
import json

from front import config


def get_report():

    def _decorate(row):
        if not row:
            return {}
        try:
            value = json.loads(row[1])
        except ValueError:
            return {}

        return {
            'id': row[0],
            't': value['T'],
            'h': value['H'],
            'pm': value['D'],
            'ch': value['G']
        }

    connection = sqlite3.connect(config.DB_PATH)
    cursor = connection.cursor()

    cursor.execute('''SELECT * FROM `stats`
        WHERE `consumed` = 0
        ORDER BY `created` DESC LIMIT 1;''')
    ret = _decorate(cursor.fetchone())

    if not ret:
        return None

    cursor.execute('''UPDATE `stats`
        SET `consumed` = 1
        WHERE `id` = :id;''', {'id': ret['id']})
    connection.commit()

    return ret
