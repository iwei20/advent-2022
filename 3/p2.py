import sys
sys.path.append("..")
from adventio import IStream
from collections import *
from itertools import *
from more_itertools import *

cin = IStream("in")

lines = cin.all_lines()

s = 0
for i in range(0, len(lines), 3):
    a = lines[i]
    b = lines[i + 1]
    c = lines[i + 2]

    for item in set(a).intersection(set(b)).intersection(set(c)):
        if (item.islower()):
            s += ord(item) - ord('a') + 1
        else:
            s += ord(item) - ord('A') + 27

print(s)

print(sum(ord(set(a).intersection(set(b)).intersection(set(c)).pop()) - (ord('a') - 1 if set(a).intersection(set(b)).intersection(set(c)).pop().islower() else ord('A') - 27) for a, b, c in grouper(lines, 3)))


