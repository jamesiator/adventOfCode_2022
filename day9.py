#!/usr/bin/python3

from inputs import day9 as input

UP = 'U'
DOWN = 'D'
LEFT = 'L'
RIGHT = 'R'

# load the movement instructions
movements = [(i.split(' ')[0], int(i.split(' ')[1])) for i in input.split('\n')]

