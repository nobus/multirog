#!/usr/bin/env python
# -*- coding: utf-8 -*-

import cjson
import websocket


def encoder(f):
    def wrapper(params):
        try:
            return cjson.encode(f(params))
        except:
            return ""

    return wrapper


def decoder(f):
    def wrapper(params):
        try:
            return cjson.decode(f(params))
        except:
            return ""

    return wrapper


@encoder
def login_request(login):
    return {"login": login}


@encoder
def exit_request(key, login):
    return {"exit": login}


@encoder
def move_request(direct):
    return {"move": direct}


@decoder
def rec_v(ws):
    return ws.recv()


def main():
    url = "ws://localhost:8888/websock"

    #websocket.enableTrace(True)
    ws = websocket.create_connection(url)

    ws.send(login_request("nobus1"))
    result = rec_v(ws)
    print "login result:", result
    key = result["login"].get("key", False)

    if key:
        ws.send(exit_request("bobus"))
        result = rec_v(ws)
        print "exit result:", result

        ws.send(move_request("up"))
        result = rec_v(ws)
        print "move result:", result

        ws.send(exit_request("nobus1"))
        result = rec_v(ws)
        print "exit result:", result
    else:
        print "not get key from server"

    ws.close()


if __name__ == "__main__":
    main()
