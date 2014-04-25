#!/usr/bin/env python
# -*- coding: utf-8 -*-

import cjson
import websocket


def encoder(f):
    def wrapper(*args, **kwargs):
        try:
            return cjson.encode(f(*args, **kwargs))
        except:
            return ""

    return wrapper


def decoder(f):
    def wrapper(*args, **kwargs):
        try:
            return cjson.decode(f(*args, **kwargs))
        except:
            return ""

    return wrapper


@encoder
def login_request(login, passwd):
    return {"login": login, "password": passwd}


@encoder
def exit_request(key, login):
    return {"key": key, "exit": login}


@encoder
def move_request(key, direct):
    return {"key": key, "move": direct}


@decoder
def rec_v(ws):
    return ws.recv()


def main():
    url = "ws://localhost:8888/websock"

    #websocket.enableTrace(True)
    ws = websocket.create_connection(url)

    ws.send(login_request("nobus1", "qqqqq"))
    result = rec_v(ws)
    print "login result:", result
    key = result["login"].get("key", False)

    if key:
        ws.send(exit_request(key, "bobus"))
        result = rec_v(ws)
        print "exit result:", result

        ws.send(move_request(key, "up"))
        result = rec_v(ws)
        print "move result:", result

        ws.send(exit_request(key, "nobus1"))
        result = rec_v(ws)
        print "exit result:", result
    else:
        print "not get key from server"

    ws.close()


if __name__ == "__main__":
    main()
