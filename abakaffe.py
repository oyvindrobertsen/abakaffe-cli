#!/usr/bin/python
# -*- coding: latin-1 -*-
from __future__ import print_function
import urllib2
import simplejson
import sys
from urlparse import urljoin
from datetime import datetime

API_URL = "http://kaffe.abakus.no/api/"


def get_json(url):
    req = urllib2.Request(url)
    opener = urllib2.build_opener()
    f = opener.open(req)
    return simplejson.load(f)


def main():
    status_json = get_json(urljoin(API_URL, "status"))
    coffee = status_json['coffee']
    on = coffee['status']
    last_start = coffee['last_start']

    last_start = coffee['last_start']
    last_start = last_start.split(' ')
    last_start_date = last_start[0]
    last_start_time = last_start[1]
    last_start_date = last_start_date.split('-')
    last_start_time = last_start_time.split(':')
    dt = datetime(int(last_start_date[0]), int(last_start_date[1]),
                  int(last_start_date[2]), int(last_start_time[0]),
                  int(last_start_time[1]))

    delta = datetime.now() - dt

    hours, minutes, seconds = str(delta).split(':')

    if on:
        print("Kaffetrakteren er på!")

    if int(hours) > 23:
        print("Det er ingen som har traktet kaffe i dag.")
    else:
        print("Kaffe ble sist traktet for " + hours + " timer siden, " + minutes
          + " minutter siden.")

    # Prints a beautiful graph displaying Abakus' coffee consumption problem
    if len(sys.argv) > 1 and sys.argv[1] == "stats":
        stats_json = get_json(urljoin(API_URL, "stats"))
        stats = stats_json['stats']

        for date, value in stats.iteritems():
            print(date + " |" + (int(value) * "#") + " " + value)


if __name__ == '__main__':
    main()
