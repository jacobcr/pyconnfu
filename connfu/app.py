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
        streamstypes.index(stream)
        streams[streamstypes.index(stream)][1].index(event)
        self.stream = stream
        self.event = event

    def callback(self, message):
        pass
        
