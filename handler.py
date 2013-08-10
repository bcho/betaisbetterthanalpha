#coding: utf-8

import time
import sqlite3
import SocketServer
from ConfigParser import ConfigParser


config = ConfigParser()
config.read('config.ini')
BUFSIZE = int(config.get('relay', 'bufsize'))


class RequestHandler(SocketServer.BaseRequestHandler):
    '''A simple TCP request handler for communicating
    with ardunio client.'''

    def setup(self):
        self.connection = sqlite3.connect(config.get('db', 'name'))

    def finish(self):
        self.connection.commit()
        self.connection.close()

    def handle(self):
        '''Just forward all the operations to wechat layer'''

        while True:
            payload = self.request.recv(BUFSIZE)

            if payload:
                self.store_stats(payload.strip())

                print payload

                command = self.get_command()
                if command:
                    self.request.sendall(command['value'])
                    self.consume_command(command['id'])
            else:
                time.sleep(1)

    def consume_command(self, _id):
        '''mark a command as consumed'''

        cursor = self.connection.cursor()
        cursor.execute('''UPDATE `jobs`
        SET `consumed` = 1
        WHERE `id` = :id;''', {'id': _id})
        self.connection.commit()

    def get_command(self):
        '''get one latest command'''

        def _decorate(row):
            if not row:
                return {}
            return {
                'id': row[0],
                'value': row[1]
            }

        cursor = self.connection.cursor()
        cursor.execute('''SELECT * FROM `jobs`
            WHERE `consumed` = 0
            ORDER BY `created` DESC LIMIT 1;''')
        return _decorate(cursor.fetchone())

    def store_stats(self, stats):
        cursor = self.connection.cursor()
        cursor.execute('''INSERT INTO `stats` (`value`)
        VALUES(:value)''', {'value': stats})
        self.connection.commit()
