import sys
sys.path.append("..")
from adventio import IStream
from collections import *
from itertools import *
from more_itertools import *
from parse import compile
import numpy as np

cin = IStream("in")
lines = cin.all_lines()

pattern = compile("Valve {} has flow rate={:d}; tunnels leads to valves {}")

END = 30

flow = dict()
adj = dict()
opened = defaultdict(bool)

def as_num(letters: str):
    return (ord(letters[0]) - ord('A')) * 26 + ord(letters[1]) - ord('A')

for line in lines:
    line = line.replace("tunnel ", "tunnels ")
    line = line.replace("valve ", "valves ")
    line = line.replace("lead ", "leads ")
    r = pattern.parse(line)

    flow[as_num(r[0])] = r[1]
    adj[as_num(r[0])] = list(map(as_num, r[2].split(", ")))

real_adj = dict()

for node, friends in adj.items():
    if flow[node] == 0 and node != as_num("AA"):
        continue
    visited = defaultdict(bool)
    real_adj[node] = dict()
    bfs = deque()
    bfs.append((node, 0))
    visited[node] = True
    while bfs:
        n, d = bfs.popleft()
        if flow[n] != 0 or n == as_num("AA"):
            real_adj[node][n] = d
        for friend in adj[n]:
            if not visited[friend]:
                bfs.append((friend, d + 1))
                visited[friend] = True

# print(real_adj[as_num("AA")])
valves = list(real_adj.keys())
aa_loc = valves.index(as_num("AA"))
# print(valves)
dp = [[(0, aa_loc) for _ in range(1 << len(valves))] for i in range(60)]

for i in range(30):
    for j in range(1 << len(valves)):
        value, curr_location = dp[i][j]
        for x in range(len(valves)):
            if not (j & (1 << x)):
                # print(valves[x], valves[curr_location])
                new_minutes = i + real_adj[valves[x]][valves[curr_location]] + 1
                new_value = value + (30 - new_minutes) * flow[valves[x]]
                dp[new_minutes][j ^ (1 << x)] = max(dp[new_minutes][j ^ (1 << x)], (new_value, x))

print(max(flatten(dp)))