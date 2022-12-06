import sys
sys.path.append("..")
from adventio import IStream
from collections import *
from itertools import *
from more_itertools import *
from parse import compile

cin = IStream("in")

lines = cin.all_lines()

for line in lines:
    for i, word in enumerate(windowed(line, 14)):
        if len(set(word)) == 14:
            print(i + 14)
            break
