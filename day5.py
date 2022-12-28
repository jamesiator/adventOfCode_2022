#!/usr/bin/python3

from inputs import day5 as input

# PART = 1
PART = 2

starting_config, instructions_list = input.split('\n\n')

# set up containers data structure
rows = starting_config.split('\n')
cols = rows[len(rows)-1].replace(' ','')
containers = {int(i): [] for i in cols}

# populate containers
for i in range(len(rows)-1):
  col = 1
  for j in range(0,len(rows[i]),4):
    if rows[i][j] == '[':
      containers[col].append(rows[i][j+1])
    col += 1
# reverse containers
for col in containers:
  containers[col].reverse()

if PART == 1:
  # execute instructions
  for instruction in instructions_list.split('\n'):
    if len(instruction) != 0:
      info = instruction.split(' ')
      qty = int(info[1])
      fromCol = int(info[3])
      toCol = int(info[5])

      for i in range(qty):
        containers[toCol].append(containers[fromCol].pop())
else:
  for instruction in instructions_list.split('\n'):
    if len(instruction) != 0:
      info  = instruction.split(' ')
      qty = int(info[1])
      fromCol = int(info[3])
      toCol = int(info[5])

      move = containers[fromCol][len(containers[fromCol])-qty:]
      containers[fromCol] = containers[fromCol][:len(containers[fromCol])-qty]
      containers[toCol] += move

result = ''
for col in containers:
  result += containers[col].pop()

print(result)