#!/usr/bin/python
#-*- coding: utf-8 -*-
u'''
Created on 4 Oct 2011

@author: jacob <jcr@tid.es>
'''
from os import listdir, path
import imp
import logging
logger = logging.getLogger()

from connfu.app import App

MODULE_EXTENSIONS = ('.py', '.pyc', '.pyo')

def package_contents(package_name):
    file, pathname, description = imp.find_module(package_name)
    if file:
        raise ImportError('Not a package: %r', package_name)
    # Use a set because some may be both source and compiled.
    return set([path.splitext(module)[0]
        for module in listdir(pathname)
        if module.endswith(MODULE_EXTENSIONS)])

def getapps(appspath = 'apps'):
    modules = package_contents(appspath)
    apps =[]

    for module in modules:
        apps.extend(getappinstance(module, appspath))

    return apps

def getappinstance(module, appspath):
    apps = []
    appmodule = __import__("%s.%s" % (appspath, module),None,None,[appspath])

    for elem in appmodule.__dict__:
        attr = appmodule.__getattribute__(elem)
        if type(attr) is type and App in attr.__bases__:
            try:
                app = attr()
                apps.append(app)
            except (KeyError, TypeError, ValueError), e:
                logger.warning("APP_LOADING_ERROR: Could not load app '%s' '%s'" % (attr.__name__, e.message))

    return apps
