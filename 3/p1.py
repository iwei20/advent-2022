import sys
sys.path.append("..")
from adventio import IStream
from collections import *
from itertools import *

cin = IStream("in")

lines = cin.all_lines()

sum = 0
for line in lines:
    firsthalf = line[:len(line)//2]
    secondhalf = line[len(line)//2:]

    for item in set(firsthalf).intersection(set(secondhalf)):
        if (item.islower()):
            sum += ord(item) - ord('a') + 1
        else:
            sum += ord(item) - ord('A') + 27

print(sum)


