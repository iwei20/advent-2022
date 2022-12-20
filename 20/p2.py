import sys
sys.path.append("..")
from adventio import IStream
from collections import *
from itertools import *
from more_itertools import *
from parse import compile
import numpy as np
import math

cin = IStream("in")
arr = cin.all_ints()
arr = [item * 811589153 for item in arr]

arr_uniq = []
freq = defaultdict(int)
for i, val in enumerate(arr):
    arr_uniq.append((val, freq[val]))
    freq[val] += 1

arr_uniq_shuffle = arr_uniq.copy()
for _ in range(10):
    for val in arr_uniq:
        # print(arr_uniq_shuffle)
        i = arr_uniq_shuffle.index(val)
        num_swaps = abs(val[0]) % (len(arr_uniq) - 1)
        # print(new_idx)
        if val[0] == 0:
            continue
        direction = (val[0]) // abs(val[0])
        for _ in range(num_swaps):
            if (i == 0 and direction == -1) or (i == len(arr_uniq) - 1 and direction == 1):
                temp = arr_uniq_shuffle[len(arr_uniq_shuffle) - 1]
                arr_uniq_shuffle[len(arr_uniq_shuffle) - 1] = arr_uniq_shuffle[0]
                arr_uniq_shuffle[0] = temp
            else:
                temp = arr_uniq_shuffle[i]
                arr_uniq_shuffle[i] = arr_uniq_shuffle[(i + direction) % len(arr_uniq_shuffle)]
                arr_uniq_shuffle[(i + direction) % len(arr_uniq_shuffle)] = temp
            i += direction
            i %= len(arr_uniq)
    # print(arr_uniq_shuffle)
    # print()
# print(arr_uniq_shuffle)
zero = arr_uniq_shuffle.index((0, 0))
zero_1k = (zero + 1000) % len(arr_uniq)
zero_2k = (zero + 2000) % len(arr_uniq)
zero_3k = (zero + 3000) % len(arr_uniq)
results = [arr_uniq_shuffle[zero_1k][0], arr_uniq_shuffle[zero_2k][0], arr_uniq_shuffle[zero_3k][0]]

print(results)
print(sum(results))