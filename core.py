#!/usr/bin/env python
# -*- coding: utf-8 -*-

import cjson
import tornado.ioloop
import tornado.web
from tornado import websocket

from world import World

'''
Protocol prototype.
Commands:
- login
- exit
- move_(up, down, left, right)
- loc_map
- players

Examples:
-> {"login": "nobus"}
<- {"map": [], "players: []}

-> {"move_up": 1}
<- {"move_up": "ok"}
-> {"move_up": 1}
<- {"move_up": "ok"}
-> {"move_up": 1}
<- {"move_up": "ok", "map": [], "players: []}

-> {"exit": "nobus"}

'''


class Game:
    def __init__(self):
        self.clients = []
        self.world = World()

    def add_client(self, client):
        self.clients.append(client)

    def del_client(self, client):
        try:
            self.clients.remove(client)
        except Exception, e:
            print e

game = Game()


class EchoWebSocket(websocket.WebSocketHandler):
    def open(self):
        print "WebSocket opened"
        game.add_client(self)

    def on_message(self, message):
        try:
            data = cjson.decode(message)
            self.write_message(cjson.encode(data))
        except Exception, e:
            req = cjson.encode({"error": e})
            self.write_message(req)

    def on_close(self):
        print "WebSocket closed"
        game.del_client(self)


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
