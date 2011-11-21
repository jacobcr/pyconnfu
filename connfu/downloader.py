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

_keepconn = True
_mhandler = []
_headers = {}

def settoken(token):
    global _headers
    _headers = {'authorization': token}


def register_mhandler(func, *args, **kw):
    _mhandler.append((func, args, kw))

def readURL(url, headers, queue):
    req = urllib2.Request(url, headers=headers)
    response = urllib2.urlopen(req) 
    line = response.readline()
    while line and _keepconn:
        queue.put(line)
        line = response.readline()
    queue.put(StopIteration)
    
def stop():
    global _keepconn
    _keepconn = False

def dispatch(q):
    for item in q:
        try:
            for func,args,kw in _mhandler:
                try:
                    func(item, *args, **kw)
                except:
                    import traceback
                    print("Error calling messagecallback (%s): %s" % (func, traceback.print_exc()))
        finally:
            q.task_done()

def init():
    q = JoinableQueue()
    greenletdispatcher = spawn(dispatch, q)
    greenletsource = spawn(readURL, baseURL, _headers, q)
    return greenletdispatcher
