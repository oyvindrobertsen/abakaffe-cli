# -*- coding: latin-1 -*-
import urllib2
import simplejson

req = urllib2.Request("http://kaffe.abakus.no/api/status")
opener = urllib2.build_opener()
f = opener.open(req)
json = simplejson.load(f)
coffee = json['coffee']
on = coffee['status']
last_start = coffee['last_start']

if on:
    print "Traktern er på"

print "Kaffe ble sist traktet kl: " + last_start
