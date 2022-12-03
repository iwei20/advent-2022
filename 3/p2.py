import sys
sys.path.append("..")
from adventio import IStream
from collections import *
from itertools import *

cin = IStream("in")

lines = cin.all_lines()

sum = 0
for i in range(0, len(lines), 3):
    a = lines[i]
    b = lines[i + 1]
    c = lines[i + 2]

    for item in set(a).intersection(set(b)).intersection(set(c)):
        if (item.islower()):
            sum += ord(item) - ord('a') + 1
        else:
            sum += ord(item) - ord('A') + 27

print(sum)


