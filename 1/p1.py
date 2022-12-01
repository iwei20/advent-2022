from adventio import IStream

cin = IStream()

import sys
sys.path.append("..")
from adventio import IStream

cin = IStream("in")

lines = cin.all_lines()

eats = []
curr_sum = 0
for line in lines:
    if line.strip():
        curr_sum += int(line)
    else:
        eats.append(curr_sum)
        curr_sum = 0

eats.sort()
print(eats[-1])
