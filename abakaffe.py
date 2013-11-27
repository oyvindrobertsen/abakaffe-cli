#!/usr/bin/python
# -*- coding: latin-1 -*-
import urllib2
import simplejson
from datetime import timedelta, datetime

req = urllib2.Request("http://kaffe.abakus.no/api/status")
opener = urllib2.build_opener()
f = opener.open(req)
json = simplejson.load(f)
coffee = json['coffee']
on = coffee['status']
last_start = coffee['last_start']
last_start = last_start.split(' ')
last_start_date = last_start[0]
last_start_time = last_start[1]
last_start_date = last_start_date.split('-')
last_start_time = last_start_time.split(':')
dt = datetime(int(last_start_date[0]), int(last_start_date[1]), int(last_start_date[2]), int(last_start_time[0]), int(last_start_time[1]))

delta = datetime.now() - dt

hours, minutes, seconds = str(delta).split(':')



if on:
    print "Kaffetrakteren er på!"


print "Kaffe ble sist traktet for " + hours + " timer siden, " + minutes + " minutter siden."
