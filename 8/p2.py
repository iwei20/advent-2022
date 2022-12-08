import sys
sys.path.append("..")
from adventio import IStream
from collections import *
from itertools import *
from more_itertools import *
from parse import compile

cin = IStream("in")
lines = cin.all_lines()

treemap = [[int(c) for c in line] for line in lines]
visible = [[False for _ in line] for line in lines]

scores = []
for r in range(len(treemap)):
    for c in range(len(treemap[0])):
        score = 1

        upscore = 0
        rightscore = 0
        leftscore = 0
        downscore = 0
        for up in range(r - 1, -1, -1):
            upscore += 1
            if (treemap[up][c] >= treemap[r][c]):
                break
        score *= upscore

        for right in range(c + 1, len(treemap[0])):
            rightscore += 1
            if (treemap[r][right] >= treemap[r][c]):
                break
        score *= rightscore

        for left in range(c - 1, -1, -1):
            leftscore += 1
            if (treemap[r][left] >= treemap[r][c]):
                break
        score *= leftscore

        for down in range(r + 1, len(treemap)):
            downscore += 1
            if (treemap[down][c] >= treemap[r][c]):
                break
        score *= downscore
        scores.append(score)
print(max(scores))