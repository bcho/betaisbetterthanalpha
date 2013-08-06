#coding: utf-8

import SocketServer
from ConfigParser import ConfigParser


config = ConfigParser()
config.read('config.ini')
BUFSIZE = config.get('relay', 'bufsize')


class RequestHandler(SocketServer.BaseRequestHandler):

    def handle(self):
        data = self.request.recv(BUFSIZE)
        self.request.sendall(data)
