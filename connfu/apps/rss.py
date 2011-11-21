#!/usr/bin/python
#-*- coding: utf-8 -*-
u'''
Created on 4 Oct 2011

@author: jacob <jcr@tid.es>
'''

from connfu.app import App

class RssApp(App):
    def __init__(self):
        App.__init__(self, 'rss', 'new')
    def callback(self, message):
        print message
