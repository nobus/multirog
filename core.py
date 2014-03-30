#!/usr/bin/env python
# -*- coding: utf-8 -*-

import tornado.ioloop
import tornado.web


class VersionHandler(tornado.web.RequestHandler):
    def get(self):
        self.write("MultiROG - Multi Rouge Online Game")


def main():
    application = tornado.web.Application([
        (r"/version", VersionHandler),
    ])

    application.listen(8888)
    tornado.ioloop.IOLoop.instance().start()


if __name__ == "__main__":
    main()
