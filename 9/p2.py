import sys
sys.path.append("..")
from adventio import IStream
from collections import *
from itertools import *
from more_itertools import *
from parse import compile

cin = IStream("in")
lines = cin.all_lines()

moves = {
    "R": (1, 0),
    "U": (0, 1),
    "D": (0, -1),
    "L": (-1, 0)
}

knots = [(0, 0) for i in range(10)]
all_tail_pos = set()

def delta(a, b):
    return (b[0] - a[0], b[1] - a[1])

def move(a, delta):
    return (a[0] + delta[0], a[1] + delta[1])

for line in lines:
    finput = line.split()
    action = moves[finput[0]]
    iterations = int(finput[1])

    for _ in range(iterations):
        knots[0] = move(knots[0], action)
        for i in range(1, 10):
            diff = delta(knots[i], knots[i - 1])
            if abs(diff[0]) > 1 or abs(diff[1]) > 1:
                updated = False
                for dx, dy in product([-1, 0, 1], [-1, 0, 1]):
                    candidate = move(knots[i], (dx, dy))
                    canddiff = delta(knots[i - 1], candidate)
                    if abs(canddiff[0]) + abs(canddiff[1]) == 1:
                        knots[i] = candidate
                        updated = True
                        break
                if updated:
                    continue
                for dx, dy in product([-1, 0, 1], [-1, 0, 1]):
                    candidate = move(knots[i], (dx, dy))
                    canddiff = delta(knots[i - 1], candidate)
                    if abs(canddiff[0]) + abs(canddiff[1]) == 2:
                        knots[i] = candidate
                        break

        all_tail_pos.add(knots[-1])
    """
    grid = [["." for c in range(40)] for r in range(40)]

    for i, (x, y) in enumerate(knots):
        grid[-(y + 20)][x + 20] = str(i)
    grid[20][20] = "s"
    for row in grid:
        print(''.join(row))
    """
        

print(len(all_tail_pos))
"""
grid = [["." for c in range(40)] for r in range(40)]

for x, y in all_tail_pos:
    grid[-(y + 20)][x + 20] = "#"
grid[20][20] = "s"
for row in grid:
    print(''.join(row))
"""