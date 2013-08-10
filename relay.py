#coding: utf-8

import time
import threading
import SocketServer
from ConfigParser import ConfigParser

from handler import RequestHandler


config = ConfigParser()
config.read('config.ini')
HOST, PORT = config.get('relay', 'host'), int(config.get('relay', 'port'))


class ThreadedTCPServer(SocketServer.ThreadingMixIn, SocketServer.TCPServer):
    allow_reuse_address = True


def main():
    server = ThreadedTCPServer((HOST, PORT), RequestHandler)

    server_thread = threading.Thread(target=server.serve_forever)
    server_thread.daemon = True
    server_thread.start()

    try:
        while True:
            time.sleep(2)
    except KeyboardInterrupt:
        print 'bye'
        #server.shutdown()


if __name__ == '__main__':
    main()
