import sys
from typing import List
sys.path.append("..")
from adventio import IStream
from collections import *
from itertools import *
from more_itertools import *
from parse import compile
from functools import cmp_to_key

cin = IStream("in")
lines = cin.all_lines()

def cmp(v1, v2):
    # print(v1, v2)
    if type(v1) == int and type(v2) == int and v1 == v2:
        return None
    if type(v1) == int and type(v2) == int and v1 < v2:
        return 1
    if type(v1) == int and type(v2) == int and v1 > v2:
        return -1
    if type(v1) == int:
        return cmp([v1], v2)
    if type(v2) == int:
        return cmp(v1, [v2])
    for i in range(len(v1)):
        if i >= len(v2):
            return -1

        result = cmp(v1[i], v2[i])
        # print(v1[i], v2[i])
        # print(result)
        if result is not None:
            return result
    if len(v1) == len(v2):
        return None
    return 1

noblank = [eval(line) for line in lines if line]
noblank.append([[2]])
noblank.append([[6]])

noblank.sort(key=cmp_to_key(cmp), reverse=True)
print(noblank)
print((noblank.index([[2]]) + 1) * (noblank.index([[6]]) + 1))