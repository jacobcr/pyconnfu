#!/usr/bin/python
#-*- coding: utf-8 -*-
u'''
Created on 4 Oct 2011

@author: jacob <jcr@tid.es>
'''
from gevent import Greenlet

from connfu import downloader
from connfu import loader
from connfu.parser import parse

class ConnfuClient(object):
    def __init__(self):
        self.apps = loader.getapps()
        downloader.register_mhandler(self.message)

    def message(self, message):
        stream, event, message = parse(message)
        for app in self.apps:
            if stream == app.stream and event == app.event:
                app.callback(message)

    def run(self):
        dispatcher = downloader.init()
        stopper = Greenlet(downloader.stop)

        stopper.start_later(5)

        dispatcher.join()


def main():
    connfuclient = ConnfuClient()
    connfuclient.run()


    
if __name__ == '__main__':
    main()
