#!/usr/bin/python -tt
# Copyright 2010 Google Inc.
# Licensed under the Apache License, Version 2.0
# http://www.apache.org/licenses/LICENSE-2.0

# Google's Python Class
# http://code.google.com/edu/languages/google-python-class/

"""A tiny Python program to check that Python is working.
Try running this program from the command line like this:
  python hello.py
  python hello.py Alice
That should print:
  Hello World -or- Hello Alice
Try changing the 'Hello' to 'Howdy' and run again.
Once you have that working, you're ready for class -- you can edit
and run Python code; now you just need to learn Python!
"""

import sys

def Cat(filename):
    f = open(filename, 'rU') ## U ignores DOS or Unix line endings
    for line in f:
        print line,  ### the trailing comma at the end inhibits the new line
### it deals with each line independently
    f.close()

def Read_file(filename):
    f = open(filename, 'rU')
    lines = f.readlines() ### reads the entire file into memory as a python list of lines, where each element in the list is one line from the file.
    print lines
    f.close()

def Read_file2(filename):

    f = open(filename, 'rU')
    text = f.read() ### this reads the entire file into one line of string

# Define a main() function that prints a little greeting.
def main():
    Cat(sys.argv[1])
  # Get the name from the command line, using 'World' as a fallback.
  if len(sys.argv) >= 2:
    name = sys.argv[1]
  else:
    name = 'World'
  print 'Hello', name

# This is the standard boilerplate that calls the main() function.
if __name__ == '__main__':
  main()
