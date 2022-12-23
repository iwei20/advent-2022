import sys
sys.path.append("..")
from adventio import IStream
from collections import *
from itertools import *
from more_itertools import *
from parse import compile
import numpy as np
import math
import operator

cin = IStream("in")

max_len = 0
maze_input = []

lines = cin.all_lines()
for line in lines[:-2]:
    if max_len == 0:
        maze_input.append(line)
    else:
        maze_input.append("".join(padded(line, " ", max_len)))
    if len(line) > max_len:
        max_len = len(line)
        maze_input = ["".join(padded(item, " ", max_len)) for item in maze_input]

space = set()
walls = set()
row_bounds = []
for r, row in enumerate(maze_input):
    start = None
    end = None
    for c, ele in enumerate(row):
        if ele == '.':
            if start is None:
                start = c
            space.add((r, c))
        if ele == '#':
            if start is None:
                start = c
            walls.add((r, c))
        if ele == " " and start is not None and end is None:
            end = c - 1
    if end is None:
        end = max_len - 1
    row_bounds.append((start, end))

col_bounds = []
for c in range(len(maze_input[0])):
    start = None
    end = None
    for r, row in enumerate(maze_input):
        ele = row[c]
        if ele == '.':
            if start is None:
                start = r
        if ele == '#':
            if start is None:
                start = r
        if ele == " " and start is not None and end is None:
            end = r - 1
    if end is None:
        end = len(maze_input) - 1
    col_bounds.append((start, end))

cw = {
    (0, 1): (1, 0),
    (1, 0): (0, -1),
    (0, -1): (-1, 0),
    (-1, 0): (0, 1)
}

ccw = {
    (0, 1): (-1, 0),
    (-1, 0): (0, -1),
    (0, -1): (1, 0),
    (1, 0): (0, 1)
}

curr = (0, row_bounds[0][0])
direction = (0, 1)
instructions = lines[-1]
curr_instruction = ""
for char in instructions:
    if char.isalpha():
        # Walk
        for i in range(int(curr_instruction)):
            next_spot = (curr[0] + direction[0], curr[1] + direction[1])
            if next_spot not in walls and next_spot not in space:
                if direction == (0, 1):
                    next_spot = (next_spot[0], row_bounds[next_spot[0]][0])
                if direction == (0, -1):
                    next_spot = (next_spot[0], row_bounds[next_spot[0]][1])
                if direction == (1, 0):
                    next_spot = (col_bounds[next_spot[1]][0], next_spot[1])
                if direction == (-1, 0):
                    next_spot = (col_bounds[next_spot[1]][1], next_spot[1])                                  
            if next_spot in walls:
                break
            curr = next_spot
        # Turn
        if char == "L":
            direction = ccw[direction]
        if char == "R":
            direction = cw[direction]
        curr_instruction = ""
    else:
        curr_instruction += char
# Walk
for i in range(int(curr_instruction)):
    next_spot = (curr[0] + direction[0], curr[1] + direction[1])
    if next_spot not in walls and next_spot not in space:
        if direction == (0, 1):
            next_spot = (next_spot[0], row_bounds[next_spot[0]][0])
        if direction == (0, -1):
            next_spot = (next_spot[0], row_bounds[next_spot[0]][1])
        if direction == (1, 0):
            next_spot = (col_bounds[next_spot[1]][0], next_spot[1])
        if direction == (-1, 0):
            next_spot = (col_bounds[next_spot[1]][1], next_spot[1])                                  
    if next_spot in walls:
        break
    curr = next_spot

idx = {
    (0, 1): 0,
    (1, 0): 1,
    (0, -1): 2,
    (-1, 0): 3
}

print(1000 * (curr[0] + 1) + 4 * (curr[1] + 1) + idx[direction])