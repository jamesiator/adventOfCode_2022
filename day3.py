#!/usr/bin/python3.10

def getPriorityValue(char):
  # if lowercase
  if ord(char) > 96:
    return ord(char) - 96
  
  # else if uppercase
  return ord(char) - 38

def getDuplicateItem(rucksack):
  items = set()
  # record every distinct item found in compartment 1
  for i in range(len(rucksack[1])):
    items.add(rucksack[1][i])

  # look through compartment 2's contents and report the duplicate
  for i in range(len(rucksack[2])):
    if rucksack[2][i] in items:
      return rucksack[2][i]

def getGroupBadge(group):
  concat = f'{group[0][1]}{group[0][2]}'
  items = set(concat[i] for i in range(len(concat)))

  items2 = set()
  concat = f'{group[1][1]}{group[1][2]}'
  for i in range(len(concat)):
    if concat[i] in items:
      items2.add(concat[i])

  concat = f'{group[2][1]}{group[2][2]}'
  for i in range(len(concat)):
    if concat[i] in items2:
      return concat[i]

groups = []

with open('day3.txt') as f:
  lines = f.readlines()
  group = []
  for line in lines:
    if line != "\n":
      items = line[:len(line)-1]
      group.append({
        1: items[:int(len(items)/2)],
        2: items[int(len(items)/2):]
      })
      if len(group) == 3:
        groups.append(group)
        group = []

prioritySum = 0

# part 1 #########################
# for group in groups:
#   for rucksack in group:
#     prioritySum += getPriorityValue(getDuplicateItem(rucksack))

# part 2 #########################
for group in groups:
  prioritySum += getPriorityValue(getGroupBadge(group))

print(f'Sum of priority values = {prioritySum}')
