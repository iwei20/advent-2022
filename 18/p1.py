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

delta = set()
delta.update(permutations((0, 0, 1)))
delta.update(permutations((0, 0, -1)))

def add(t1, t2):
    return (t1[0] + t2[0], t1[1] + t2[1], t1[2] + t2[2])

print(list(delta))
cubes = set()
for line in lines:
    cubes.add(eval(f"({line})"))

surface = 6 * len(cubes)
for cube in cubes:
    for d in delta:
        if add(cube, d) in cubes:
            surface -= 1
print(surface)