import sys
sys.path.append("..")
from adventio import IStream
from collections import *
from itertools import *
from more_itertools import *
from parse import compile

cin = IStream("in")
lines = iter(cin.all_lines())

noop_pattern = compile("noop")
addx_pattern = compile("addx {:d}")

x = 1
ans = 0
addx_iter = 0

curr = None
rn = None
ra = None

cycle = 0
while cycle < 220:
    if ra is not None:
        addx_iter += 1
        if addx_iter == 2:
            addx_iter = 0
            x += ra[0]
            curr = next(lines)
    else:
        curr = next(lines)
    rn = noop_pattern.parse(curr)
    ra = addx_pattern.parse(curr)

    cycle += 1
    if cycle in [20, 60, 100, 140, 180, 220]:
        ans += x * cycle

print(ans)