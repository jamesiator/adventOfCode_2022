#!/usr/bin/python

elves = []
# mostCals = 0

with open('day1.txt') as f:
  lines = f.readlines()
  cals = 0
  for line in lines:
    if line == "\n":
      # mostCals = max(mostCals, cals)
      elves.append(cals)
      cals = 0
    else:
      cals += int(line)

elves.sort(reverse=True)
print(f'Top 3 elves by calory count: 1- {elves[0]}; 2- {elves[1]}; 3- {elves[2]}')
print(f'Total of top 3 = {elves[0] + elves[1] + elves[2]}')