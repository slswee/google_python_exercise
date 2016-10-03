#!/usr/bin/python
# Copyright 2010 Google Inc.
# Licensed under the Apache License, Version 2.0
# http://www.apache.org/licenses/LICENSE-2.0

# Google's Python Class
# http://code.google.com/edu/languages/google-python-class/

import sys
import re
import os
import shutil
import commands

"""Copy Special exercise
"""

# +++your code here+++
# Write functions and modify main() to call them
def ListSpecial(dir): # find all the special files, and list them
    filenames = os.listdir(dir)
    results = []
    print filenames
    for filename in filenames:
        match = re.search(r'\w+__\w+__[.]\w+', filename)
        if match:
            path = os.path.join(dir, filename)
            path = os.path.abspath(path)
            #print path
            results.append(path)
        # the else statement is for debugging
        #else:
        #    print 'not found'
    return results
##find the special files, create the todir directory if it doesn't exist
def CopyToDir(todir, dir):
    filenames = os.listdir(dir)
    if not os.path.exists(todir):
        os.mkdir(todir)
    for filename in filenames:
        match = re.search(r'\w+__\w+__[.]\w+', filename)
        if match:
            shutil.copy(filename, todir)
    return

def ZipToDir(zipname, dir):
    zip -j zipname ListSpecial(dir)
    return 
#    zip -j blah.zip file_paths



def main():
  # This basic command line argument parsing code is provided.
  # Add code to call your functions below.

  # Make a list of command line arguments, omitting the [0] element
  # which is the script itself.
  args = sys.argv[1:]
  if not args:
    print "usage: [--todir dir][--tozip zipfile] dir [dir ...]";
    sys.exit(1)

  # todir and tozip are either set from command line
  # or left as the empty string.
  # The args array is left just containing the dirs.
  todir = ''
  if args[0] == '--todir':
    todir = args[1]
    del args[0:2]

  tozip = ''
  if args[0] == '--tozip':
    tozip = args[1]
    del args[0:2]

  if len(args) == 0:
    print "error: must specify one or more dirs"
    sys.exit(1)

  # +++your code here+++
  # Call your functions

  specialfiles = ListSpecial(args[0])
  for f in specialfiles:
      print f
  #CopyToDir(todir, args[0])

if __name__ == "__main__":
  main()
