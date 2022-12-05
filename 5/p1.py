import sys
sys.path.append("..")
from adventio import IStream
from collections import *
from itertools import *
from more_itertools import *
from parse import compile

cin = IStream("in")

lines = cin.all_lines()
lines = lines[10:]

stacks = [
    "BZT",
    "VHTDN",
    "BFMD",
    "TJGWVQL",
    "WDGPVFQM",
    "VZQGHFS",
    "ZSNRLTCW",
    "ZHWDJNRM",
    "MQLFDS",
]

stackslists = [list(string) for string in stacks]

pattern = compile("move {:d} from {:d} to {:d}")

for line in lines:
    r = pattern.parse(line)
    for i in range(r[0]):
        stackslists[r[2] - 1].append(stackslists[r[1] - 1].pop())

print(''.join([stacklist[-1] for stacklist in stackslists]))