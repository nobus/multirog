#!/usr/bin/env python
# -*- coding: utf-8 -*-


import websocket


def main():
    url = "ws://localhost:8888/websock"
    websocket.enableTrace(True)
    ws = websocket.create_connection(url)
    ws.send("Hello, World")
    result = ws.recv()
    print "Result: ", result
    ws.close()


if __name__ == "__main__":
    main()
