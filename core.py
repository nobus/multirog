#!/usr/bin/env python
# -*- coding: utf-8 -*-

import cjson
import tornado.ioloop
import tornado.web
from tornado import websocket

clients = []


class EchoWebSocket(websocket.WebSocketHandler):
    def open(self):
        print "WebSocket opened"
        clients.append(self)

    def on_message(self, message):
        try:
            data = cjson.decode(message)
            self.write_message(cjson.encode(data))
        except Exception, e:
            req = cjson.encode({"error": e})
            self.write_message(req)

    def on_close(self):
        print "WebSocket closed"
        clients.remove(self)


class StatHandler(tornado.web.RequestHandler):
    def get(self):
        stat = "MultiROG - Multi Rouge Online Game\n"
        stat += "Version 0.1.0\n"
        self.write(stat)


def main():
    application = tornado.web.Application([
        (r"/stat", StatHandler),
        (r"/websock", EchoWebSocket),
    ])

    application.listen(8888)
    tornado.ioloop.IOLoop.instance().start()


if __name__ == "__main__":
    main()
