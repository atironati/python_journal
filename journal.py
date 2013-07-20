#! /usr/bin/env python
import sys, tempfile, os
import datetime
from subprocess import call

print "hello world"

EDITOR = os.environ.get('EDITOR','vim') #that easy!

initial_message = "" # if you want to set up the file somehow

now = datetime.datetime.now()

directory = "entries/%d/%s/" % (now.year, now.strftime("%B"))
if not os.path.exists(directory):
    os.makedirs(directory)
filename = "%s%d.txt" % (directory, now.day)

print filename

entry_for_today = open(filename,'w')

with tempfile.NamedTemporaryFile(suffix=".tmp") as tempfile:
    tempfile.write(initial_message)
    tempfile.flush()
    call([EDITOR, tempfile.name])
    # do the parsing with `tempfile` using regular File operations

    with open(tempfile.name, 'r') as tf:
        # save tempfile as journal entry
        for line in tf.readlines():
            sys.stdout.write(line)
            entry_for_today.write(line)

    entry_for_today.close()
