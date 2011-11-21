#!/usr/bin/python
#-*- coding: utf-8 -*-
u'''
Created on 4 Oct 2011

@author: jacob <jcr@tid.es>
'''


streams = [('voice',['join','leave']), 
        ('twitter', ['new']), 
        ('rss', ['new']), 
        ('sms', ['new'])]
streamstypes = [x[0] for x in streams]

class App(object):
    def __init__(self, stream, event):
        self.stream = streams[streamstypes.index(stream)]
        self.event = self.stream[1].index(event)

    def callback(message):
        pass
        
