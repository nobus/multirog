#!/usr/bin/env python
# -*- coding: utf-8 -*-

import time
import random

import cjson
import tornado.ioloop
import tornado.web
from tornado import websocket

from md5 import md5

from world import World

'''
Protocol prototype.
Commands:
- login
- exit
- move (up, down, left, right)
- loc_map
- players

Examples:
-> {"login": "nobus"}
<- {"key": hash, "map": [], "players: []}

-> {"key": hash, "move": "up"}
<- {"key": hash, "move": "ok_up"}
-> {"key": hash, "move": "up"}
<- {"key": hash, "move": "not_up"}
-> {"key": hash, "move": "ok_up"}
<- {"key": hash, "move": "ok_up", "map": [], "players: []}

-> {"key": hash, "exit": "nobus"}

'''


class Game:
    def __init__(self):
        self.clients = []
        self.players = {}

        self.world = World()

    def add_client(self, client):
        self.clients.append(client)

    def del_client(self, client):
        try:
            self.clients.remove(client)
        except Exception, e:
            print e

    def get_key(self, login):
        h = md5("%s%s%s" % (login, time.time(), random.random()))
        return h.hexdigest()

    def proto_login(self, client, value):
        k = self.get_key(value)
        self.players[k] = (client, value)
        return {"key": k, "map": [], "players": []}

    def proto_key(self, client, key):
        if key in self.players:
            if client == self.players[key][0]:
                return True

        return False

    def proto_exit(self, client, value):
        try:
            del self.players[value]
            return value
        except Exception, e:
            print e
            return "error player: %s" % value

    def proto_move(self, client, value):
        return "ok_%s" % value

    def process_data(self, client, data):
        ret = {}

        if "key" in data and "login" not in data:
            key = data.pop("key")
            if not self.proto_key(client, key):
                return {"key": "error key"}
                return ret
        elif "key" not in data and "login" in data:
            pass
        else:
            return {"key": "error key"}

        for cmd, value in data.iteritems():
            f = getattr(self, "proto_%s" % cmd)
            if callable(f):
                ret[cmd] = f(client, value)
            else:
                ret[cmd] = "error command protocol"

        return ret

    def notify(self, client, data):
        if type(data) == dict:
            return self.process_data(client, data)
        else:
            return {"error": "need dict"}

game = Game()


class EchoWebSocket(websocket.WebSocketHandler):
    def open(self):
        print "WebSocket opened"
        game.add_client(self)

    def on_message(self, message):
        try:
            data = cjson.decode(message)
            resp = game.notify(self, data)
            self.write_message(cjson.encode(resp))
        except:
            req = cjson.encode({"error": "undefined"})
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
