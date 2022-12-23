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
import heapq

cin = IStream("in")
lines = cin.all_lines()

walls = set()
blizzards = [set() for _ in range(4)]

start = (0, 1)
end = (len(lines) - 1, len(lines[0]) - 2)

dir_to_index = {
    "^": 0,
    "<": 1,
    "v": 2,
    ">": 3,
}

indices_to_delta = {
    0: (-1, 0),
    1: (0, -1),
    2: (1, 0),
    3: (0, 1),
}

reset = {
    0: lambda t: (len(lines) - 2, t[1]),
    1: lambda t: (t[0], len(lines[0]) - 2),
    2: lambda t: (1, t[1]),
    3: lambda t: (t[0], 1)
}

def add(a, b):
    return (a[0] + b[0], a[1] + b[1])

blizzard_dp = {0: blizzards}

for r, row in enumerate(lines):
    for c, ele in enumerate(row):
        if ele == "#":
            walls.add((r, c))
        if ele in dir_to_index:
            blizzards[dir_to_index[ele]].add((r, c))

# dists = [[1e9 for ele in row] for row in lines]
frontier = set()
frontier.add(start)
deltas = [(-1, 0), (0, -1), (1, 0), (0, 1), (0, 0)]
# dists[start[0]][start[1]] = 0
minute = 0
while end not in frontier:
    next_frontier = set()
    # calc next blizzard state
    next_blizzards = []
    for i, delta in indices_to_delta.items():
        next_blizzards_dir = set()
        for blizzard in blizzard_dp[minute][i]:
            new_blizzard = add(blizzard, delta)
            if new_blizzard in walls or new_blizzard == start or new_blizzard == end:
                new_blizzard = reset[i](new_blizzard)
            next_blizzards_dir.add(new_blizzard)
        next_blizzards.append(next_blizzards_dir)
    blizzard_dp[minute + 1] = next_blizzards
    # look to next minute
    for r, c in frontier:
        for delta in deltas:
            new_r, new_c = add((r, c), delta)
            if 0 <= new_r < len(lines) and 0 <= new_c < len(lines[0]) and (new_r, new_c) not in flatten(blizzard_dp[minute + 1]) and (new_r, new_c) not in walls:
                next_frontier.add((new_r, new_c))
    frontier = next_frontier
    minute += 1

print(minute)