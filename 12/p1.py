import sys
sys.path.append("..")
from adventio import IStream
from collections import *
from itertools import *
from more_itertools import *
from parse import compile

cin = IStream("in")
lines = cin.all_lines()

startpos = (0, 0)
endpos = (0, 0)

visited = [[False for item in line] for line in lines]

bfs = deque()
for r in range(len(lines)):
    for c in range(len(lines[0])):
        if lines[r][c] == 'S':
            startpos = (r, c)
        if lines[r][c] == 'E':
            endpos = (r, c)

bfs.append((0, startpos))
visited[startpos[0]][startpos[1]] = True

def inbounds(r, c):
    return 0 <= r < len(lines) and 0 <= c < len(lines[0])

while bfs:
    steps, pos = bfs.popleft()
    if pos == endpos:
        print(steps)
        break
    for dr, dc in [(0, 1), (1, 0), (-1, 0), (0, -1)]:
        if inbounds(pos[0] + dr, pos[1] + dc) and not visited[pos[0] + dr][pos[1] + dc] and (ord(lines[pos[0] + dr][pos[1] + dc]) <= ord(lines[pos[0]][pos[1]]) + 1 or lines[pos[0] + dr][pos[1] + dc] == 'E' or lines[pos[0]][pos[1]] == 'S'):
            bfs.append((steps + 1, (pos[0] + dr, pos[1] + dc)))
            visited[pos[0] + dr][pos[1] + dc] = True

