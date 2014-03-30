#!/usr/bin/env python
# -*- coding: utf-8 -*-

import tornado.ioloop
import tornado.web
from tornado import websocket


class StatHandler(tornado.web.RequestHandler):
    def get(self):
        stat = "MultiROG - Multi Rouge Online Game\n"
        stat += "Version 0.1.0\n"
        self.write(stat)


class EchoWebSocket(websocket.WebSocketHandler):
    def open(self):
        print "WebSocket opened"

    def on_message(self, message):
        self.write_message(u"You said: " + message)

    def on_close(self):
        print "WebSocket closed"


def main():
    application = tornado.web.Application([
        (r"/stat", StatHandler),
        (r"/websock", EchoWebSocket),
    ])

    application.listen(8888)
    tornado.ioloop.IOLoop.instance().start()


if __name__ == "__main__":
    main()
