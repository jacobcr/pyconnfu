#!/usr/bin/python
#-*- coding: utf-8 -*-
u'''
Created on 4 Oct 2011

@author: jacob <jcr@tid.es>
'''

from unittest import TestCase
from connfu.app import App


class TestApp(TestCase):
    def testRssOk(self):
        '''if rss and event new'''
        App('rss', 'new')

    def testRssKo(self):
        '''if rss and event new'''
        self.assertRaises(ValueError, App, 'rss', 'invalid')

    def testInvalidStream(self):
        '''if stream invalid exception'''
        self.assertRaises(ValueError, App, 'invalid', 'new')

    def testSmsOk(self):
        '''if sms and event new'''
        App('sms', 'new')

    def testSmsKo(self):
        '''if sms and event new'''
        self.assertRaises(ValueError, App, 'sms', 'invalid')
        

