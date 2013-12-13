#!/usr/bin/python
# -*- coding: latin-1 -*-
from __future__ import print_function
from argparse import ArgumentParser
from lib import Abakaffe


def get_args():
    parser = ArgumentParser(description="When was the coffee brewed?",
                            prog='abakaffe')
    parser.add_argument('-a', '--ascii', action='store_true', default=False,
                        dest='ascii', help='prints the Abakaffe ascii-art')
    parser.add_argument('-s', '--stats', action='store_true', default=False,
                        dest='stats',
                        help="prints a graph displaying Abakus' coffee "
                             "consumption")
    parser.add_argument('-o', '--online', action='store_true', default=False,
                        dest='online',
                        help="should I go one floor down to Online?")
    parser.add_argument('-v', '--version', action='version',
                        version='%(prog)s ' + Abakaffe.get_version(),
                        dest='version', help='prints the abakaffe-cli version '
                                             'number')
    return parser.parse_args()


def main():
    args = get_args()
    print(Abakaffe.abakus(args))
    if args.stats:
        print(Abakaffe.abakus_stats())
    if args.online:
        print(Abakaffe.online())

if __name__ == '__main__':
    main()
