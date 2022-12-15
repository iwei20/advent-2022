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

pattern = compile("Sensor at x={:d}, y={:d}: closest beacon is at x={:d}, y={:d}")

loc_to_dist = dict()
sensors = set()
beacons = set()
def man_dist(t1, t2):
    return abs(t1[0] - t2[0]) + abs(t1[1] - t2[1])

for line in lines:
    result = pattern.parse(line)
    loc_to_dist[(result[0], result[1])] = man_dist((result[0], result[1]), (result[2], result[3]))
    sensors.add((result[0], result[1]))
    beacons.add((result[2], result[3]))

loc_to_start = dict()

for loc, dist in loc_to_dist.items():
    loc_to_start[loc] = loc[1] - dist

count = 0
# ROW = 10
ranges = []
for loc, start in loc_to_start.items():
    # print(start)
    if start < 0:
        ranges.append((loc[0] + start, loc[0] - start, loc))
ranges.sort()
# print(ranges)

def solve():
    global ranges
    for i in range(int(4e6) + 1):
        for loc, start in loc_to_start.items():
            if i == start:
                ranges.append((loc[0], loc[0], loc)) # inclusive

                # print(ranges[-1])
        
        ranges.sort()
        range_check = [ranges[0]]
        for r in range(1, len(ranges)):
            merged = False
            for nr in range(len(range_check)):
                if ranges[r][0] <= range_check[nr][1] and range_check[nr][0] <= ranges[r][1]:
                    range_check[nr] = (min(ranges[r][0], range_check[nr][0]), max(ranges[r][1], range_check[nr][1]))
                    merged = True
                    break
            if not merged:
                range_check.append(ranges[r])
        
        for r in range_check:
            if 0 <= r[1] < int(4e6):
                return (r[1] + 1, i)

        new_ranges = []
        for r in ranges:
            if r[0] == r[1] and i >= r[2][1]:
                continue
            if r[2][1] <= i:
                new_ranges.append((r[0] + 1, r[1] - 1, r[2]))
            else:
                new_ranges.append((r[0] - 1, r[1] + 1, r[2]))

        ranges = new_ranges
        # if (i < 10):
            # print(ranges)

result = [thing for thing in solve()]
print(result[0] * int(4e6) + result[1])
