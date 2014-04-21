#!/usr/bin/env python
# -*- coding: utf-8 -*-

import cjson
import websocket


def get_request(login):
    req = {}
    req["login"] = login
    req["action"] = "move_up"

    return cjson.encode(req)


def main():
    url = "ws://localhost:8888/websock"

    #websocket.enableTrace(True)
    ws = websocket.create_connection(url)
    ws.send(get_request("nobus1"))
    result = ws.recv()

    try:
        result = cjson.decode(result)
    except Exception, e:
        print e

    print "Result: ", result
    ws.close()


if __name__ == "__main__":
    main()
