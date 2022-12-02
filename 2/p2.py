import sys
sys.path.append("..")
from adventio import IStream
from collections import *
from itertools import *

cin = IStream("in")

lines = cin.all_lines()

scores = {
    "A X": 3+0,
    "B X": 1+0,
    "C X": 2+0,
    "A Y": 1+3,
    "B Y": 2+3,
    "C Y": 3+3,
    "A Z": 2+6,
    "B Z": 3+6,
    "C Z": 1+6,
}

print(sum(scores[i] for i in lines))
