#coding: utf-8

import time
import threading
import SocketServer

from handler import RequestHandler


from config.relay import HOST, PORT


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
        server.shutdown()


if __name__ == '__main__':
    main()
