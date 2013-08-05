#coding: utf-8

import SocketServer

from config.relay import BUFSIZE


class RequestHandler(SocketServer.BaseRequestHandler):

    def handle(self):
        data = self.request.recv(BUFSIZE)
        self.request.sendall(data)
