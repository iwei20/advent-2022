import sys
sys.path.append("..")
from adventio import IStream
from collections import *
from itertools import *
from more_itertools import *
from parse import compile

cin = IStream("in")
lines = cin.all_lines()

treemap = [[int(c) for c in line] for line in lines]
visible = [[False for _ in line] for line in lines]

for r in range(len(treemap)):
    visible[r][0] = True
    visible[r][-1] = True
    maxsofar = treemap[r][0]
    for c in range(1, len(treemap[0])):

        if maxsofar < treemap[r][c]:
            visible[r][c] = True
            maxsofar = treemap[r][c]
    maxsofar = treemap[r][-1]
    for c in range(len(treemap[0]) - 2, 0, -1):

        if maxsofar < treemap[r][c]:
            visible[r][c] = True
            maxsofar = treemap[r][c]


for c in range(len(treemap[0])):
    visible[0][c] = True
    visible[-1][c] = True
    maxsofar = treemap[0][c]
    for r in range(1, len(treemap)):
        if maxsofar < treemap[r][c]:
            visible[r][c] = True
            maxsofar = treemap[r][c]
    maxsofar = treemap[-1][c]
    for r in range(len(treemap) - 2, 0, -1):

        if maxsofar < treemap[r][c]:
            visible[r][c] = True
            maxsofar = treemap[r][c]

print(visible)
print(list(collapse(visible)).count(True))