# encoding: utf-8
from __future__ import unicode_literals
from urllib.parse import urljoin
from urllib.request import urlopen, Request
import simplejson
from datetime import datetime
from .version import __version__


class Abakaffe():
    ABA_ASCII = '''
        ____              _           _          __  __
      .'    `.      /\   | |         | |        / _|/ _|
     /        \    /  \  | |__   __ _| | ____ _| |_| |_ ___
     |        |   / /\ \ | '_ \ / _` | |/ / _` |  _|  _/ _ \ 
     \        /  / ____ \| |_) | (_| |   < (_| | | | ||  __/
      `.____.'  /_/    \_\_.__/ \__,_|_|\_\__,_|_| |_| \___|
    '''

    ABA_API_URL = "https://kaffe.abakus.no/api/"
    ONLINE_API_URL = "http://draug.online.ntnu.no/"

    @staticmethod
    def get_version():
        '''
        Returns the current version by reading the version.py file.
        '''
        return __version__

    @staticmethod
    def get_file(api_base, api_module):
        '''
        Returns a file object of the server response.
        '''
        url = urljoin(api_base, api_module)
        req = Request(url, headers={'User-Agent' : "Magic Browser"}) 
        con = urlopen(req)
        data = con.read() 
        return data


    @staticmethod
    def get_status(time_delta, organization="Abakus"):
        '''
        Builds a message based on a datetime.timedelta object and an
        organization.
        '''
        message = ""
        if int(time_delta.days):
            message += "Det er ingen som har traktet kaffe i dag."
        else:
            hours = time_delta.seconds // (60 * 60)
            minutes = (time_delta.seconds // 60) % 60

            if not hours and not minutes:
                return "Kaffen til {organization} ble nettopp traktet! \
                        LØØØP!!!".format(organization=organization)

            message += "Kaffen til {organization} ble sist traktet for ".format(organization=organization)
            if hours:
                if hours == 1:
                    message += "én time"
                else:
                    message += str(hours) + " timer"
            if hours and minutes:
                message += " og "
            if minutes:
                if minutes == 1:
                    message += "ett minutt "
                else:
                    message += str(minutes) + " minutter "
            message += "siden."
        return message

    @staticmethod
    def abakus(args=None):
        '''
        Main Abakus function, ties together the message returned by get_status
        with other message components based on args.
        '''
        message = ""
        f = Abakaffe.get_file(Abakaffe.ABA_API_URL, 'status')
        status_json = simplejson.loads(f)
        coffee = status_json['coffee']
        on = coffee['status']
        last_start = coffee['last_start']
        last_start = datetime.strptime(last_start, "%Y-%m-%d %H:%M")
        time_delta = datetime.now() - last_start

        if args.ascii:
            message += Abakaffe.ABA_ASCII + "\n"

        if on:
            message += "Kaffetrakteren er på!\n"

        message += Abakaffe.get_status(time_delta)
        return message

    @staticmethod
    def abakus_stats():
        '''
        Returns a stats-message with a bargraph based on the Abakus coffeestats
        API node.
        '''
        message = ""
        f = Abakaffe.get_file(Abakaffe.ABA_API_URL, 'stats')
        stats_json = simplejson.loads(f)
        stats = stats_json['stats']
        for date in sorted(stats.keys()):
            value = int(stats[date])
            message += "%s %s %s \n" % (date, value * u"\u2588", value)
        return message

    @staticmethod
    def online():
        raise NotImplementedError
        '''
        Returns a message with info from the Online coffee API,
        total pots brewed today, and last time brewed.
        '''
        message = ""
        f = Abakaffe.get_file(Abakaffe.ONLINE_API_URL, "coffee.txt")
        total_today = int(f.readline())
        if total_today > 0:
            message += "Online har traktet %s kanner i dag.\n" % total_today
        else:
            message += "Online har ikke traktet kaffe i dag.\n"
        last_start = f.readline()
        last_start = datetime.strptime(last_start, "%d. %B %Y %H:%M:%S")
        time_delta = datetime.now() - last_start
        message += Abakaffe.get_status(time_delta, "Online")
        return message
