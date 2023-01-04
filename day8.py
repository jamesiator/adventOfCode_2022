#!/usr/bin/python3

from inputs import day8 as input

# input = '''092357
# 164821
# 237967
# 986210
# 674218'''

PART1 = True

rows = input.split('\n')
numRows = len(rows)
numCols = len(rows[0])

treeMap = [[int(j) for j in rows[i]] for i in range(numRows)]

def isVisible(row, col):
  return isVisible_above(row,col) or isVisible_below(row,col) or isVisible_left(row,col) or isVisible_right(row,col)

def isVisible_above(row, col):
  '''
  check all trees to the north for trees that would block the view
  '''
  for a in range(row):
    if treeMap[a][col] >= treeMap[row][col]:
      return False
  return True

def isVisible_below(row, col):
  '''
  check all trees to the south for trees that would block the view
  '''
  # print(f'isVisible_below w/ row {row} and col {col}')
  for b in range(row+1, numRows):
    # print(f'checking row {b} against row {row}')
    if treeMap[b][col] >= treeMap[row][col]:
      return False
  return True

def isVisible_left(row, col):
  '''
  check all trees to the west for trees that would block the view
  '''
  for c in range(col):
    if treeMap[row][c] >= treeMap[row][col]:
      return False
  return True

def isVisible_right(row, col):
  '''
  check all trees to the east for trees that would block the view
  '''
  for d in range(col+1, numCols):
    if treeMap[row][d] >= treeMap[row][col]:
      return False
  return True

visible = numRows * 2 + (numCols-2) * 2
for i in range(1, numRows-1):
  for j in range(1, numCols-1):
    if isVisible(i,j):
      visible += 1

print(visible)
