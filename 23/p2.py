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
lines = cin.all_lines()

deltas = set(product([-1, 0, 1], [-1, 0, 1]))
deltas.remove((0, 0))

elves = set()

for r, row in enumerate(lines):
    for c, ele in enumerate(row):
        if ele == "#":
            elves.add((r, c))

def add(a, b):
    return (a[0] + b[0], a[1] + b[1])

def north(elf):
    if all(add(elf, d) not in elves for d in deltas if d[0] == -1):
        return add(elf, (-1, 0))

def south(elf):
    if all(add(elf, d) not in elves for d in deltas if d[0] == 1):
        return add(elf, (1, 0))

def west(elf):
    if all(add(elf, d) not in elves for d in deltas if d[1] == -1):
        return add(elf, (0, -1))

def east(elf):
    if all(add(elf, d) not in elves for d in deltas if d[1] == 1):
        return add(elf, (0, 1))

def print_grid():
    for i in range(-10, 15):
        print("".join("#" if (i, j) in elves else "." for j in range(-10, 15)))

dir_decisions = [north, south, west, east]

will_continue = True
round_game = 0
while will_continue:
    will_continue = False
    # key = target, value = from
    proposals = defaultdict(list)
    for elf in elves:
        if all(add(elf, d) not in elves for d in deltas):
            proposals[elf].append(elf)
            continue
        moved = False
        for dec in dir_decisions:
            result = dec(elf)
            if result:
                proposals[result].append(elf)
                moved = True
                will_continue = True
                break
        if not moved:
            proposals[elf].append(elf)

    new_elves = set()
    for proposal, applicants in proposals.items():
        if len(applicants) > 1:
            new_elves.update(applicants)
        else:
            new_elves.add(proposal)
    elves = new_elves
    dir_decisions.append(dir_decisions.pop(0))
    round_game += 1
    # print_grid()
    # print()

print(round_game)