#!/usr/bin/python3

from inputs import day7 as input

# PART1 = True
PART1 = False

dirs = {'/': 0}
dirPath = []

# go through temrinal output
for line in input.split('\n'):
  info = line.split(' ')

  # make sure we're pointing at the correct dir
  if info[0] == '$':
    if info[1] == 'cd':
      if info[2] == '..':
        dirPath.pop()
      else:
        # //some/dir/name format to account for duplicate names
        dirPath.append('/'.join(dirPath)+info[2])

  # record any discovered dirs
  elif info[0] == 'dir':
    # //some/dir/name format to account for duplicate names
    dirs['/'.join(dirPath)+info[1]] = 0

  # add file sizes to all containing dirs
  else:
    for dir in dirPath:
      dirs[dir] += int(info[0])

if PART1:
  # sum dirs with less than 100k storage
  space = 0
  for dir in dirs:
    if dirs[dir] <= 100000:
      space += dirs[dir]

  print(space)
else:
  spaceNeeded = dirs['/'] - 40000000
  space = 30000000

  for dir in dirs:
    if dirs[dir] >= spaceNeeded and dirs[dir] < space:
      space = dirs[dir]

  print(space)