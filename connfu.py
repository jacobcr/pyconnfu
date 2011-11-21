#!/usr/bin/python
#-*- coding: utf-8 -*-
u'''
Created on 4 Oct 2011

@author: jacob <jcr@tid.es>
'''

from gevent import monkey; monkey.patch_all(thread=False)
from gevent import spawn
from gevent.event import Event
from gevent.queue import JoinableQueue, Queue
from unittest import TestCase

import urllib2

baseURL = "https://stream.connfu.com/connfu-stream-testing-emc2"
headers = {'authorization': "none"}


def readURL(url, headers, queue):
    req = urllib2.Request(url, headers=headers)
    response = urllib2.urlopen(req) 
    line = response.readline()
    while line:
        queue.put(line)
        line = response.readline()
    queue.put(StopIteration)
    
def dispatch(q):
    while True:
        try:
            item = q.get()
            print item
        finally:
            q.task_done()

def main():
    q = JoinableQueue()
    greenletdispatcher = spawn(dispatch, q)
    greenletsource = spawn(readURL, baseURL, headers, q)
    greenletdispatcher.join()


    
if __name__ == '__main__':
    main()

        

