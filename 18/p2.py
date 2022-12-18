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
delta = list(delta)

def add(t1, t2):
    return (t1[0] + t2[0], t1[1] + t2[1], t1[2] + t2[2])

cubes = set()
for line in lines:
    cubes.add(eval(f"({line})"))

surface = 0
inside = set()
# Loop through each cube
for cube in cubes:
    # Consider each adjacent space
    for d in delta:
        candidate_outside = add(cube, d)
        # If that space is empty
        if candidate_outside not in cubes:

            # Check if it is in the interior by bfsing and seeing if it hits (25, 0, 0)
            if candidate_outside in inside:
                continue

            hit_50 = False
            visited = set()
            bfs = deque()
            bfs.append(candidate_outside)
            visited.add(candidate_outside)
            while bfs:
                front = bfs.popleft()
                if 25 in front or -1 in front:
                    hit_50 = True
                    break
                for d_check in delta:
                    neighbor = add(front, d_check)
                    if neighbor not in visited and neighbor not in cubes:
                        bfs.append(neighbor)
                        visited.add(neighbor)
            
            # If it is not in the interior, then we are done
            if hit_50:
                surface += 1
            else:
                inside.update(visited)
print(surface)