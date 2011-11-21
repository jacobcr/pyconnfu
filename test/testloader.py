#!/usr/bin/python
#-*- coding: utf-8 -*-
u'''
Created on 4 Oct 2011

@author: jacob <jcr@tid.es>
'''

from unittest import TestCase
from os import path

from connfu import loader

class TestLoader(TestCase):
    def testGetInstance(self):
        apps = loader.getappinstance('ok', 'apps')
        self.assertEquals(1, len(apps))

    def testGetInstanceKo(self):
        apps = loader.getappinstance('ko', 'apps')
        self.assertEquals(0, len(apps))

    def testGetApps(self):
        apps = loader.getapps('apps')
        self.assertEquals(1, len(apps))
