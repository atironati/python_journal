#! /usr/bin/env python
import sys, tempfile, os
import datetime
from subprocess import call
import argparse

parser = argparse.ArgumentParser()
group = parser.add_mutually_exclusive_group()
group.add_argument('--open', '-o', action='store', dest='open',
                   help='open a journal entry for a given day')
group.add_argument('--recent', '-r', nargs='?', action='store', dest='recent', const=10, type=int,
                   help='display recent journal entries, defaults to 10')

args = parser.parse_args()

def hello_world(stron):
    print str(stron)

# Create a journal entry for the current day or
# edit today's entry if it already exists
def entry_for_today():
    EDITOR = os.environ.get('EDITOR','vim') #that easy!
    now = datetime.datetime.now()

    directory = "entries/%d/%s/" % (now.year, now.strftime("%B"))
    if not os.path.exists(directory):
        os.makedirs(directory)
    filename = "%s%d.txt" % (directory, now.day)

    call([EDITOR, filename])

if args.open:
    hello_world(args.open)
elif args.recent:
    hello_world(args.recent)
else:
    entry_for_today()


