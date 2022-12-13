import sys
from typing import List
sys.path.append("..")
from adventio import IStream
from collections import *
from itertools import *
from more_itertools import *
from parse import compile

cin = IStream("in")
lines = cin.all_lines()

def cmp(v1, v2):
    # print(v1, v2)
    if type(v1) == int and type(v2) == int and v1 == v2:
        return None
    if type(v1) == int and type(v2) == int and v1 < v2:
        return True
    if type(v1) == int and type(v2) == int and v1 > v2:
        return False
    if type(v1) == int:
        return cmp([v1], v2)
    if type(v2) == int:
        return cmp(v1, [v2])
    for i in range(len(v1)):
        if i >= len(v2):
            return False

        result = cmp(v1[i], v2[i])
        # print(v1[i], v2[i])
        # print(result)
        if result is not None:
            return result
    if len(v1) == len(v2):
        return None
    return True


correct = []
for i, (first, second, _) in enumerate(grouper(lines, 3)):
    fp: List[int] = eval(first)
    sp: List[int] = eval(second)
    # print(cmp(fp, sp))
    if cmp(fp, sp):
        correct.append(i + 1)

print(correct)
print(sum(correct))