#!/usr/bin/python3

from inputs import day8 as input

# input = \
# '''30373
# 25512
# 65332
# 33549
# 35390'''

PART1 = False

ROWS = input.split('\n')
NUM_ROWS = len(ROWS)
NUM_COLS = len(ROWS[0])

TREE_MAP = [[int(j) for j in ROWS[i]] for i in range(NUM_ROWS)]

def isVisible(row, col):
  '''
  Returns true if a tree in the given row and column is visible from outside the forrest; else false
  '''

  def isVisible_above(row, col):
    '''
    check all trees to the north for trees that would block the view
    '''
    for i in range(row):
      if TREE_MAP[i][col] >= TREE_MAP[row][col]:
        return False
    return True

  def isVisible_below(row, col):
    '''
    check all trees to the south for trees that would block the view
    '''
    # print(f'isVisible_below w/ row {row} and col {col}')
    for i in range(row+1, NUM_ROWS):
      # print(f'checking row {b} against row {row}')
      if TREE_MAP[i][col] >= TREE_MAP[row][col]:
        return False
    return True

  def isVisible_left(row, col):
    '''
    check all trees to the west for trees that would block the view
    '''
    for i in range(col):
      if TREE_MAP[row][i] >= TREE_MAP[row][col]:
        return False
    return True

  def isVisible_right(row, col):
    '''
    check all trees to the east for trees that would block the view
    '''
    for i in range(col+1, NUM_COLS):
      if TREE_MAP[row][i] >= TREE_MAP[row][col]:
        return False
    return True

  return isVisible_above(row,col) or isVisible_below(row,col) or isVisible_left(row,col) or isVisible_right(row,col)

def visibility_score(row, col):
  '''
  Returns the visibility score for the tree in the given row/column
  '''

  tree = TREE_MAP[row][col]

  def visibility_above(row, col):
    visibility = 0
    for i in range(row-1, -1, -1):
      visibility += 1
      if TREE_MAP[i][col] >= tree:
        break
    return visibility

  def visibility_below(row, col):
    visibility = 0
    for i in range(row+1, NUM_ROWS):
      visibility += 1
      if TREE_MAP[i][col] >= tree:
        break
    return visibility

  def visibility_left(row, col):
    visibility = 0
    for i in range(col-1, -1, -1):
      visibility += 1
      if TREE_MAP[row][i] >= tree:
        break
    return visibility

  def visibility_right(row, col):
    visibility = 0
    for i in range(col+1, NUM_COLS):
      visibility += 1
      if TREE_MAP[row][i] >= tree:
        break
    return visibility

  above = visibility_above(row,col)
  below = visibility_below(row,col)
  left = visibility_left(row,col)
  right = visibility_right(row,col)

  # print(f'{above} x {below} x {left} x {right}')

  return above * below * left * right

if PART1:
  visible = NUM_ROWS * 2 + (NUM_COLS-2) * 2
  for i in range(1, NUM_ROWS-1):
    for j in range(1, NUM_COLS-1):
      if isVisible(i,j):
        visible += 1
  print(visible)
else:
  highest_visibility = 0
  for i in range(1, NUM_ROWS-1):
    for j in range(1, NUM_COLS-1):
      visibility = visibility_score(i,j)
      # print(f'({i}, {j}) | height = {TREE_MAP[i][j]} | visibility = {visibility}')
      highest_visibility = max(highest_visibility, visibility)
  print(f'highest visibility = {highest_visibility}')
