import sys
sys.path.append("..")
from adventio import IStream
from collections import *
from itertools import *
from more_itertools import *
from parse import compile
import numpy as np
import math

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


# Look for the period
already = dict()
jet_count = 0
i = 0
period_start = 0
period_end = 0
while True:
    if (jet_count % len(line), i % 5) not in already:
        already[(jet_count % len(line), i % 5)] = i
    elif jet_count >= 2 * len(line):
        period_start = already[(jet_count % len(line), i % 5)]
        period_end = i
        # print(jet_count % len(line), i % 5)
        break
    # Spawn the rock
    spawnpos = (2, current_height + 3)
    blocks = [add(spawnpos, delta) for delta in rocks[i % 5]]

    while True:
        # Push the rock
        move_lr = lr[next(jets)]
        jet_count += 1
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
    i += 1   



# Spawn the big rock
extra = dict()
new_height = current_height

for j in range(period_end - period_start):
    # Spawn the rock
    spawnpos = (2, new_height + 3)
    blocks = [add(spawnpos, delta) for delta in rocks[i % 5]]

    while True:
        # Push the rock
        move_lr = lr[next(jets)]
        jet_count += 1
        candidate = [add(block, move_lr) for block in blocks]
        if not any(restrict(c_b) for c_b in candidate):
            blocks = candidate
        # Rock falls
        fall = (0, -1)
        candidate = [add(block, fall) for block in blocks]
        if any(restrict(c_b) for c_b in candidate):
            stopped.update(blocks)
            new_height = max(item[1] for item in stopped) + 1
            # print(new_height)
            extra[j + 1] = new_height - current_height
            break
        else:
            blocks = candidate
            
    i += 1

height_delta = extra[period_end - period_start]
TOTAL = 1000000000000
TOTAL -= period_end
total_height = current_height
total_height += (TOTAL // (period_end - period_start)) * height_delta
# print(total_height)
TOTAL %= (period_end - period_start)
"""
# Spawn the big rock
newer_heights = [new_height]
for _ in range(10):
    newest_height = newer_heights[-1]
    for j in range(period_end - period_start):
        # Spawn the rock
        spawnpos = (2, newest_height + 3)
        blocks = [add(spawnpos, delta) for delta in rocks[i % 5]]

        while True:
            # Push the rock
            move_lr = lr[next(jets)]
            jet_count += 1
            candidate = [add(block, move_lr) for block in blocks]
            if not any(restrict(c_b) for c_b in candidate):
                blocks = candidate
            # Rock falls
            fall = (0, -1)
            candidate = [add(block, fall) for block in blocks]
            if any(restrict(c_b) for c_b in candidate):
                stopped.update(blocks)
                newest_height = max(item[1] for item in stopped) + 1
                # print(new_height)
                break
            else:
                blocks = candidate
                
        i += 1
    newer_heights.append(newest_height)
    print(jet_count % len(line), i % 5)

print([b - a for a, b in windowed(newer_heights, 2)])
"""
if TOTAL != 0:
    total_height += extra[TOTAL]
print(total_height)
