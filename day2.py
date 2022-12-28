#!/usr/bin/python3.10
import re

'''
A and X = ROCK
B and Y = PAPER
C and Z = SCISSORS
'''

ROCK = 'rock'
PAPER = 'paper'
SCISSORS = 'scissors'

ROCK_VAL = 1
PAPER_VAL = 2
SCISSORS_VAL = 3

WIN = 6
DRAW = 3
LOSS = 0

# Part1 #########################
# def flatten(move):
#   if move == 'A' or move == 'X':
#     return ROCK
#   elif move == 'B' or move == 'Y':
#     return PAPER
#   elif move == 'C' or move == 'Z':
#     return SCISSORS

# part 2 ########################
def flatten(move):
  match move:
    case 'A':
      return ROCK
    case 'B':
      return PAPER
    case 'C':
      return SCISSORS

def convert(theirMove, mine):
  if mine == 'Y': #draw
    return flatten(theirMove)

  if mine == 'X': #lose
    match theirMove:
      case 'A':
        return SCISSORS
      case 'B':
        return ROCK
      case 'C':
        return PAPER

  else: #win
    match theirMove:
      case 'A':
        return PAPER 
      case 'B':
        return SCISSORS
      case 'C':
        return ROCK

# them-me format
results = {
  f'{ROCK}-{ROCK}': ROCK_VAL + DRAW,
  f'{ROCK}-{PAPER}': PAPER_VAL + WIN,
  f'{ROCK}-{SCISSORS}': SCISSORS_VAL + LOSS,
  f'{PAPER}-{ROCK}': ROCK_VAL + LOSS,
  f'{PAPER}-{PAPER}': PAPER_VAL + DRAW,
  f'{PAPER}-{SCISSORS}': SCISSORS_VAL + WIN,
  f'{SCISSORS}-{ROCK}': ROCK_VAL + WIN,
  f'{SCISSORS}-{PAPER}': PAPER_VAL + LOSS,
  f'{SCISSORS}-{SCISSORS}': SCISSORS_VAL + DRAW
}

score = 0

with open('day2.txt') as f:
  lines = f.readlines()
  for line in lines:
    if line != "\n":
      moves = re.split(' |\n', line)
      # part 1 ######################
      # score += results[f'{flatten(moves[0])}-{flatten(moves[1])}']

      # part 2 ######################
      score += results[f'{flatten(moves[0])}-{convert(moves[0], moves[1])}']

print(f'total score = {score}')