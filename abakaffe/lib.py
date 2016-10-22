# -*- coding: latin-1 -*-
import urllib2
import simplejson
from urlparse import urljoin
from datetime import datetime
from version import __version__


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
        headers = {'User-Agent': 'abakaffe-cli'}
        req = urllib2.Request(url, headers=headers)
        opener = urllib2.build_opener()
        try:
            f = opener.open(req)
        except IOError:
            print('Kunne ikke koble til %s' % url)
            exit(0)
        return f

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

            message += "Kaffen til {organization} ble sist traktet for "
            message = message.format(organization=organization)
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
        status_json = simplejson.load(f)
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
        stats_json = simplejson.load(f)
        stats = stats_json['stats']
        for date in sorted(stats.keys())[-5:]:
            value = int(stats[date])
            message += u"{date} {graph} {value}\n".format(
                date=date,
                graph=value * u"\u2588",
                value=value)
        message = message.rstrip()  # Remove trailing whitespace
        return message

    @staticmethod
    def online():
        '''
        Returns a message with info from the Online coffee API,
        total pots brewed today, and last time brewed.
        '''
        message = ""
        f = Abakaffe.get_file(Abakaffe.ONLINE_API_URL, "coffee.txt")
        total_today = int(f.readline())
        last_start = f.readline()
        last_start = datetime.strptime(last_start, "%d. %B %Y %H:%M:%S")
        if last_start.date() == datetime.today().date() and total_today > 0:
            message += "Online har traktet {count} kanner i dag.\n".format(
                count=total_today)
            time_delta = datetime.now() - last_start
            message += Abakaffe.get_status(time_delta, "Online")
        else:
            message += "Online har ikke traktet kaffe i dag."
        return message
