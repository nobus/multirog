#!/usr/bin/env python
# -*- coding: utf-8 -*-

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
-> {"login": "nobus", "password": "qwerty"}
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

    def get_key(self):
        h = md5(str(random.random()))
        return h.hexdigest()

    def get_login_from_key(self, key):
        client, login = self.players.get(key, [False, False])

        if client and login:
            return login

    def add_player(self, client, login):
        k = self.get_key()
        self.players[k] = (client, login)
        return {"key": k, "map": [], "players": []}

    def del_player(self, key, login):
        key_login = self.get_login_from_key(key)

        if key_login and key_login == login:
            del self.players[key]
            return login
        else:
            return "error player: %s" % login

    def login(self, client, req_data):
        '''
        password - use in future
        '''
        if "password" in req_data:
            login = req_data.get("login", False)
            passwd = req_data.get("password", False)

            if login and passwd:
                return self.add_player(client, login)
            else:
                return "error login or password"
        else:
            return "password not found"

    def check_key(self, client, req_data):
        key = req_data.get("key", False)

        if key in self.players:
            if client == self.players[key][0]:
                return key

        return False

    def exit_game(self, key, req_data):
        login = req_data.get("exit", False)

        if login:
            return self.del_player(key, login)
        else:
            return "error protocol"

    def move(self, key, req_data):
        return "ok_%s" % req_data.get("move", "no")

    def process_data(self, client, data):
        ret = {}

        if "login" in data:
            return {"login": self.login(client, data)}
        elif "key" in data:
            key = self.check_key(client, data)
            if key:
                if "exit" in data:
                    return {"exit": self.exit_game(key, data)}

                if "move" in data:
                    return {"move": self.move(key, data)}
            else:
                return {"key": "error key"}
        else:
            return {"error": "please login"}

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
        except Exception, e:
            print e
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
