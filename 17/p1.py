import sys
sys.path.append("..")
from adventio import IStream
from collections import *
from itertools import *
from more_itertools import *
from parse import compile
import numpy as np

cin = IStream("in")
line = cin.next_line()

current_height = 0
rocks = {
    0: [(0, 0), (1, 0), (2, 0), (3, 0)],
    1: [(0, 1), (1, 1), (2, 1), (1, 0), (1, 2)],
    2: [(0, 0), (1, 0), (2, 0), (2, 1), (2, 2)],
    3: [(0, 0), (0, 1), (0, 2), (0, 3)],
    4: [(0, 0), (0, 1), (1, 0), (1, 1)]
}

lr = {
    '>': (1, 0),
    '<': (-1, 0)
}
stopped = set()
jets = cycle(line)

def add(t1, t2):
    return (t1[0] + t2[0], t1[1] + t2[1])

def restrict(potential) -> bool:
    return potential in stopped or potential[0] < 0 or potential[0] >= 7 or potential[1] < 0

for i in range(2022):
    # Spawn the rock
    spawnpos = (2, current_height + 3)
    blocks = [add(spawnpos, delta) for delta in rocks[i % 5]]

    while True:
        # Push the rock
        move_lr = lr[next(jets)]
        candidate = [add(block, move_lr) for block in blocks]
        if not any(restrict(c_b) for c_b in candidate):
            blocks = candidate
        # Rock falls
        fall = (0, -1)
        candidate = [add(block, fall) for block in blocks]
        if any(restrict(c_b) for c_b in candidate):
            stopped.update(blocks)
            current_height = max(item[1] for item in stopped) + 1
            break
        else:
            blocks = candidate
    
print(current_height)
