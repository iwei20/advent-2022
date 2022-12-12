import sys
sys.path.append("..")
from adventio import IStream
from collections import *
from itertools import *
from more_itertools import *
from parse import compile

cin = IStream("in")
lines = cin.all_lines()
lines = [list(line) for line in lines]

aposes = []
endpos = (0, 0)

for r in range(len(lines)):
    for c in range(len(lines[0])):
        if lines[r][c] == 'S':
            lines[r][c] = 'a'
        if lines[r][c] == 'a':
            aposes.append((r, c))
        if lines[r][c] == 'E':
            endpos = (r, c)

def inbounds(r, c):
    return 0 <= r < len(lines) and 0 <= c < len(lines[0])

minimum = 1e9
for apos in aposes:
    bfs = deque()
    visited = [[False for item in line] for line in lines]
    bfs.append((0, apos))
    visited[apos[0]][apos[1]] = True

    while bfs:
        steps, pos = bfs.popleft()
        if pos == endpos:
            minimum = min(steps, minimum)
            break
        for dr, dc in [(0, 1), (1, 0), (-1, 0), (0, -1)]:
            if inbounds(pos[0] + dr, pos[1] + dc) and not visited[pos[0] + dr][pos[1] + dc] and (ord(lines[pos[0] + dr][pos[1] + dc]) <= ord(lines[pos[0]][pos[1]]) + 1 or lines[pos[0] + dr][pos[1] + dc] == 'E' or lines[pos[0]][pos[1]] == 'S'):
                bfs.append((steps + 1, (pos[0] + dr, pos[1] + dc)))
                visited[pos[0] + dr][pos[1] + dc] = True

print(minimum)