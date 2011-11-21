#!/usr/bin/python
#-*- coding: utf-8 -*-
u'''
Created on 4 Oct 2011

@author: jacob <jcr@tid.es>
'''

from simplejson import loads, JSONDecodeError

def safeGetJson(maybe_json, key=None):
    try:
        if key:
            return loads(maybe_json).get(key)
        else:
            return loads(maybe_json)
    except (JSONDecodeError, AttributeError):
        return maybe_json

def parse(message):
    message = safeGetJson(message) 
    
    try:
        message['id']
        message['actor']
        return 'rss', 'new', message['title']
    except KeyError, e:
        print 'could not parse rss message'
        raise e
    except TypeError,e:
        return 'sms', 'new', message[1]['message']
