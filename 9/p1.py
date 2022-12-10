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

headpos = (0, 0)
tailpos = (0, 0)
all_tail_pos = set()

def delta(a, b):
    return (b[0] - a[0], b[1] - a[1])

def move(a, delta):
    return (a[0] + delta[0], a[1] + delta[1])

for line in lines:
    finput = line.split()
    action = moves[finput[0]]
    iterations = int(finput[1])
    for i in range(iterations):
        headpos = move(headpos, action)
        diff = delta(headpos, tailpos)
        if (abs(diff[0]) >= 2 and diff[1] == 0) or (diff[0] == 0 and abs(diff[1]) >= 2):
            tailpos = move(tailpos, action)
        elif abs(diff[0]) + abs(diff[1]) >= 3:
            tailpos = move(headpos, (-action[0], -action[1]))
        print(headpos, tailpos)
        all_tail_pos.add(tailpos)

print(len(all_tail_pos))
