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


# actual
cin = IStream("in")
ROWS = 50
face_offsets = [
    (0, ROWS), 
    (0, 2*ROWS),
    (ROWS, ROWS),
    (2*ROWS, 0),
    (2*ROWS, ROWS),
    (3*ROWS, 0)
]

# right, down, left, up
transfer = [
    [1, 2, 3, 5],
    [4, 2, 0, 5],
    [1, 4, 3, 0],
    [4, 5, 0, 2],
    [1, 5, 3, 2],
    [4, 1, 0, 3]
]

"""
# example
cin = IStream("sample_in")
ROWS = 4
face_offsets = [
    (0, 2 * ROWS),
    (ROWS, 0),
    (ROWS, ROWS),
    (ROWS, 2 * ROWS),
    (2 * ROWS, 2 * ROWS),
    (2 * ROWS, 3 * ROWS)
]

transfer = [
    [5, 3, 2, 1],
    [2, 4, 5, 0],
    [3, 4, 1, 0],
    [5, 4, 2, 0],
    [5, 1, 2, 3],
    [0, 1, 4, 3]
]
"""
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


faces = [[row[o_c:o_c + ROWS] for row in maze_input[o_r:o_r + ROWS]] for o_r, o_c in face_offsets]


space_face = []
walls_face = []

for face in faces:
    space = set()
    walls = set()
    for r, row in enumerate(face):
        for c, ele in enumerate(row):
            if ele == ".":
                space.add((r, c))
            if ele == "#":
                walls.add((r, c))
    space_face.append(space)
    walls_face.append(walls)

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

idx = {
    (0, 1): 0,
    (1, 0): 1,
    (0, -1): 2,
    (-1, 0): 3
}

from_idx = {
    0: (0, -1),
    1: (-1, 0),
    2: (0, 1),
    3: (1, 0)
}

transfer_dir = {
    ((0, 1), (0, 1)): lambda t: (t[0], 0),
    ((0, 1), (1, 0)): lambda t: (0, (ROWS - 1) - t[0]),
    ((0, 1), (0, -1)): lambda t: ((ROWS - 1) - t[0], (ROWS - 1)),
    ((0, 1), (-1, 0)): lambda t: ((ROWS - 1), t[0]),
    ((1, 0), (0, 1)): lambda t: ((ROWS - 1) - t[1], 0),
    ((1, 0), (1, 0)): lambda t: (0, t[1]),
    ((1, 0), (0, -1)): lambda t: (t[1], (ROWS - 1)),
    ((1, 0), (-1, 0)): lambda t: ((ROWS - 1), (ROWS - 1) - t[1]),
    ((0, -1), (0, 1)): lambda t: ((ROWS - 1) - t[0], 0),
    ((0, -1), (1, 0)): lambda t: (0, t[0]),
    ((0, -1), (0, -1)): lambda t: (t[0], (ROWS - 1)),
    ((0, -1), (-1, 0)): lambda t: ((ROWS - 1), (ROWS - 1) - t[0]),
    ((-1, 0), (0, 1)): lambda t: (t[1], 0),
    ((-1, 0), (1, 0)): lambda t: (0, (ROWS - 1) - t[1]),
    ((-1, 0), (0, -1)): lambda t: ((ROWS - 1) - t[1], (ROWS - 1)),
    ((-1, 0), (-1, 0)): lambda t: ((ROWS - 1), t[1])
}

face = 0
curr = (0, 0)
direction = (0, 1)
instructions = lines[-1]
curr_instruction = ""
for char in instructions:
    if char.isalpha():
        # Walk
        for i in range(int(curr_instruction)):
            next_spot = (curr[0] + direction[0], curr[1] + direction[1])
            next_face = face
            next_direction = direction
            if (next_spot not in walls_face[face]) and (next_spot not in space_face[face]):
                next_face = transfer[face][idx[direction]]
                next_direction = from_idx[transfer[next_face].index(face)]
                next_spot = transfer_dir[(direction, next_direction)](next_spot)
                # print(face, next_face)
                # print(direction, next_direction)
                # print(curr, next_spot)
            if next_spot in walls_face[next_face]:
                break
            curr = next_spot
            face = next_face
            direction = next_direction
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
    next_face = face
    next_direction = direction
    if next_spot not in walls_face[face] and next_spot not in space_face[face]:
        next_face = transfer[face][idx[direction]]
        next_direction = from_idx[transfer[next_face].index(face)]
        next_spot = transfer_dir[(direction, next_direction)](next_spot)
        print(face, next_face)
        print(direction, next_direction)
        print(curr, next_spot)
    if next_spot in walls_face[next_face]:
        break
    curr = next_spot
    face = next_face
    direction = next_direction

curr = (curr[0] + face_offsets[face][0], curr[1] + face_offsets[face][1])
print(1000 * (curr[0] + 1) + 4 * (curr[1] + 1) + idx[direction])