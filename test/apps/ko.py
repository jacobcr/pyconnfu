#!/usr/bin/python
#-*- coding: utf-8 -*-
u'''
Created on 4 Oct 2011

@author: jacob <jcr@tid.es>
'''

from connfu.app import App

class AppKo(App):
    def __init__(self):
        App.__init__(self, 'notfound', 'new')
    def callback(message):
        print message

class NotApp(object):
    def __init__(self):
        pass
