import sys
sys.path.append("..")
from adventio import IStream
from collections import *
from itertools import *
from more_itertools import *
from parse import compile

cin = IStream("in")

noop_pattern = compile("noop")
addx_pattern = compile("addx {:d}")

x = 1
ans = [['.' for i in range(40)] for j in range(6)]
addx_iter = 0

curr = None
rn = None
ra = None

cycle = 0
while cycle < 240:
    if ra is not None:
        addx_iter += 1
        if addx_iter == 2:
            addx_iter = 0
            x += ra[0]
            curr = cin.next_line()
    else:
        curr = cin.next_line()
    rn = noop_pattern.parse(curr)
    ra = addx_pattern.parse(curr)
    if cycle % 40 in [x - 1, x, x + 1]:
        ans[cycle // 40][cycle % 40] = "#"
    cycle += 1


for row in ans:
    print(''.join(row))