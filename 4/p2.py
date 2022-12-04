import sys
sys.path.append("..")
from adventio import IStream
from collections import *
from itertools import *
from more_itertools import *
from parse import compile

cin = IStream("in")

lines = cin.all_lines()

pattern = compile("{a:d}-{b:d},{c:d}-{d:d}")
count = 0
for line in lines:
    result = pattern.parse(line)
    if set(range(result["a"], result["b"] + 1)).intersection(set(range(result["c"], result["d"] + 1))):
        count += 1

print(count)