#!/usr/bin/env python
# -*- coding: utf-8 -*-

import tornado.ioloop
import tornado.web


class StatHandler(tornado.web.RequestHandler):
    def get(self):
        stat = "MultiROG - Multi Rouge Online Game\n"
        stat += "Version 0.1.0\n"
        self.write(stat)


def main():
    application = tornado.web.Application([
        (r"/stat", StatHandler),
    ])

    application.listen(8888)
    tornado.ioloop.IOLoop.instance().start()


if __name__ == "__main__":
    main()
