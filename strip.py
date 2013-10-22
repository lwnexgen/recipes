#!/usr/bin/python
import beautifulsoup

from optparse import OptionParser
parser = OptionParser()
(options, args) = parser.parse_args()

def usage():
    print "usage: strip.py [URL]"

if len(args) < 1:
    usage()
    exit 1


