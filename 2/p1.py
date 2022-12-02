import sys
sys.path.append("..")
from adventio import IStream
from collections import *
from itertools import *

cin = IStream("in")

lines = cin.all_lines()

scores = {
    "A X": 1+3,
    "B X": 1+0,
    "C X": 1+6,
    "A Y": 2+6,
    "B Y": 2+3,
    "C Y": 2+0,
    "A Z": 3+0,
    "B Z": 3+6,
    "C Z": 3+3,
}

print(sum(scores[i] for i in lines))
