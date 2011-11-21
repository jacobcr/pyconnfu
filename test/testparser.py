#!/usr/bin/python
#-*- coding: utf-8 -*-
u'''
Created on 4 Oct 2011

@author: jacob <jcr@tid.es>
'''

from unittest import TestCase
from os import path

from connfu.parser import parse

TESTDIR = path.abspath(path.dirname(__file__))

class TestApp(TestCase):
    def setUp(self):
        self.file = open(path.join(TESTDIR, 'sample.connfu'))

    def testMessageRssOk(self):
        line = self.file.readline()
        stream, message = parse(line)
        self.assertEquals('rss', stream)

    def testMessageSMSOk(self):
        self.file.readline()
        line = self.file.readline()
        stream, message = parse(line)
        self.assertEquals('sms', stream)

    def testComplete(self):
        for line in self.file:
            parse(line)

