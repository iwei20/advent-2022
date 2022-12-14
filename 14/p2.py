import sys
sys.path.append("..")
from adventio import IStream
from collections import *
from itertools import *
from more_itertools import *
from parse import compile
import numpy as np

cin = IStream("in")
lines = cin.all_lines()

pp = compile("{:d},{:d}")
a = np.zeros((1000, 1000))
lowest = 0
for line in lines:
    pairs = [pp.parse(pair) for pair in line.split(" -> ")]
    for start, end in windowed(pairs, 2):
        min_x = min(start[0], end[0])
        max_x = max(start[0], end[0]) + 1

        min_y = min(start[1], end[1])
        max_y = max(start[1], end[1]) + 1

        if max_y - 1 > lowest:
            lowest = max_y

        a[min_x:max_x, min_y:max_y] = 1
a[0:1000, lowest + 1] = 1

# Add sand
iterations = 0
while True:
    curr_x = 500
    curr_y = 0

    if a[curr_x, curr_y] != 0:
        break
    while True:
        if a[curr_x, curr_y + 1] == 0:
            curr_y += 1
            continue
        if a[curr_x - 1, curr_y + 1] == 0:
            curr_x -= 1
            curr_y += 1
            continue
        if a[curr_x + 1, curr_y + 1] == 0:
            curr_x += 1
            curr_y += 1
            continue
        break
    a[curr_x, curr_y] = 2
    iterations += 1

print(iterations)

