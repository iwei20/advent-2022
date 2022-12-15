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

count = 0
ROW = 2000000
# ROW = 10
for i in range(int(-1e7), int(1e7)):
    if (i, ROW) in sensors or (i, ROW) in beacons:
        continue
    for loc, dist in loc_to_dist.items():
        # print(loc)
        if man_dist(loc, (i, ROW)) <= dist:
            # print(i)
            count += 1
            break
print(count)
