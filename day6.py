#!/usr/bin/python3

from inputs import day6 as input

# PART = 1
PART = 2

def part1():
  for i in range(len(input)-4):
    if len(set(input[i:i+4])) == 4:
      return i+4

def part2():
  for i in range(len(input)-14):
    if len(set(input[i:i+14])) == 14:
      return i+14

if PART == 1:
  print(part1())
else:
  print(part2())
