#!/usr/bin/python3

from inputs import day8 as input

PART1 = True

rows = input.split('\n')
rowLen = len(rows[0])
columnLen = len(rows)

map = [[int(j) for j in rows[i]] for i in rows]

def isVisible(row, col):
  return isVisible_above(row, col) or isVisible_below(row, col) or isVisible_left(row, col) or isVisible_right(row, col)

def isVisible_above(row, col):
  '''
  check all trees to the north for trees that would block the view
  '''
  for a in range(row):
    if int(rows[a][col]) >= int(rows[row][col]):
      return False
  return True

def isVisible_below(row, col):
  '''
  check all trees to the south for trees that would block the view
  '''
  for b in range(row+1, rowLen):
    if int(rows[b][col]) >= int(rows[row][col]):
      return False
  return True

def isVisible_left(row, col):
  '''
  check all trees to the west for trees that would block the view
  '''
  for c in range(col):
    if int(rows[row][c]) >= int(rows[row][col]):
      return False
  return False

def isVisible_right(row, col):
  '''
  check all trees to the east for trees that would block the view
  '''
  for d in range(col+1, columnLen):
    if int(rows[row][d]) >= int(rows[row][col]):
      return False
  return True

visible = (rowLen) * 2 + (columnLen-2) * 2
for i in range(1, rowLen-1):
  for j in range(1, columnLen-1):
    if isVisible(i,j):
      visible += 1

print(visible)
