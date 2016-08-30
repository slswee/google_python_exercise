#!/usr/bin/python
# Copyright 2010 Google Inc.
# Licensed under the Apache License, Version 2.0
# http://www.apache.org/licenses/LICENSE-2.0

# Google's Python Class
# http://code.google.com/edu/languages/google-python-class/

import sys
import re

"""Baby Names exercise

Define the extract_names() function below and change main()
to call it.

For writing regex, it's nice to include a copy of the target
text for inspiration.

Here's what the html looks like in the baby.html files:
...
<h3 align="center">Popularity in 1990</h3>
....
<tr align="right"><td>1</td><td>Michael</td><td>Jessica</td>
<tr align="right"><td>2</td><td>Christopher</td><td>Ashley</td>
<tr align="right"><td>3</td><td>Matthew</td><td>Brittany</td>
...

Suggested milestones for incremental development:
 -Extract the year and print it
 -Extract the names and rank numbers and just print them
 -Get the names data into a dict and print it
 -Build the [year, 'name rank', ... ] list and print it
 -Fix main() to use the extract_names list
"""

def extract_names(filename):
  """
  Given a file name for baby.html, returns a list starting with the year string
  followed by the name-rank strings in alphabetical order.
  ['2006', 'Aaliyah 91', Aaron 57', 'Abagail 895', ' ...]
  """
  # +++your code here+++
  # get year
  f = open(filename, 'rU')
  text = f.read()
  m_year = re.search(r'.+Popularity\sin\s(\d\d\d\d).+', text)
  if m_year:
     # print m_year.group(1)
      year = m_year.group(1)
  else: print 'year not found'

  names_dict = {}
  names_dict[year] = ''
  names_list = []
  # get rank and name
  m_rank_name = re.findall(r'.+align..right.+td.(\d+).+td.+td.(\w+).+td..td.(\w+).+', text)
  if m_rank_name: ## rank boyname girlname, a list of tuples
      # get the names data into a dict and print it
      for tuple_item in m_rank_name:
          names_dict[tuple_item[1]] = tuple_item[0]
          names_dict[tuple_item[2]] = tuple_item[0]
  f.close()
  return names_dict

'''
  # Build the [year, 'name rank', ... ] list and print it
  names_list.append(year)
  for item in sorted(names_dict.keys()):
      names_list.append(item)
      names_list.append(names_dict[item])
'''
 # print names_list
'''
  if m_rank_name:
      print m_rank_name.group(1)
      print m_rank_name.group(2)
      print m_rank_name.group(3)
      rank = m_rank_name.group(1)
  else:
      print 'match objectg not found'
'''

def print_dict(dict):
    for item in sorted(dict.keys()):
        print item, ' ', dict[item]

def write_dict_to_file(dict, filename):
    f = open(filename, 'w')
    for item in sorted(dict.keys()):
        f.write(item + ' ' + dict[item] + '\n')
    f.close()

### I don't like putting year + names_rank in a list, because it's difficult to
# print.  Adding the year as the first entry of the name_rank dictionary solves
# this problem perfectly

'''
def write_list_to_file(namelist, filename):
    f = open(filename, 'w')
    f.write(namelist[0])
    f.write('\n')
    for i in range(1, len(namelist)-1):
        f.write(namelist[i] + ' ')
    f.close()
'''

def main():
  # This command-line parsing code is provided.
  # Make a list of command line arguments, omitting the [0] element
  # which is the script itself.
  args = sys.argv[1:]

  if not args:
    print 'usage: [--summaryfile] file [file ...]'
    sys.exit(1)

  # Notice the summary flag and remove it from args if it is present.
  summary = False
  if args[0] == '--summaryfile':
    summary = True
    del args[0]

  # +++your code here+++
  # For each filename, get the names, then either print the text output
  # or write it to a summary file
  for f in args:
      if summary == False:
          print_dict(extract_names(f))
      else:
          write_dict_to_file(extract_names(f), f+'.summary')


if __name__ == '__main__':
  main()
