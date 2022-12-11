import sys
sys.path.append("..")
from adventio import IStream
from collections import *
from itertools import *
from more_itertools import *
from parse import compile
"""
monkeys = [
    [79, 98],
    [54, 65, 75, 74],
    [79, 60, 97],
    [74]
]

ops = [
    lambda x: x * 19,
    lambda x: x + 6,
    lambda x: x * x,
    lambda x: x + 3
]

div = [
    23, 19, 13, 17
]

t_tar = [
    2, 2, 1, 0
]

f_tar = [
    3, 0, 3, 1
]
"""
realmonkies = [

]

monkeys = [
    [83, 62, 93],
    [90, 55],
    [91, 78, 80, 97, 79, 88],
    [64, 80, 83, 89, 59],
    [98, 92, 99, 51],
    [68, 57, 95, 85, 98, 75, 98, 75],
    [74],
    [68, 64, 60, 68, 87, 80, 82]
]

ops = [
    lambda x: x * 17,
    lambda x: x + 1,
    lambda x: x + 3,
    lambda x: x + 5,
    lambda x: x * x,
    lambda x: x + 2,
    lambda x: x + 4,
    lambda x: x * 19
]

div = [
    2, 17, 19, 3, 5, 13, 7, 11
]

t_tar = [
    1, 6, 7, 7, 0, 4, 3, 4
]

f_tar = [
    6, 3, 5, 2, 1, 0, 2, 5
]

for m in range(8):
    realmonkies.append([[worry % modulo for modulo in div] for worry in monkeys[m]])

item_count = [0] * 8

for r in range(10000):
    for m in range(8):
        for item in realmonkies[m]:
            item_count[m] += 1
            newlevel = [ops[m](item[sub]) % div[sub] for sub in range(8)]
            if newlevel[m] % div[m] == 0:
                realmonkies[t_tar[m]].append(newlevel)
            else:
                realmonkies[f_tar[m]].append(newlevel)
        realmonkies[m].clear()

item_count.sort()
print(item_count[-1] * item_count[-2])