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
dp = [[[(0, aa_loc, aa_loc) for _ in range(1 << len(valves))] for i in range(60)] for i in range(60)]

for i in range(26):
    for k in range(26):
        for j in range(1 << len(valves)):
            value, curr_location, elephant_location = dp[i][k][j]
            for x, y in product(range(len(valves)), range(len(valves))):
                if x != y and not (j & (1 << x)) and not (j & (1 << y)):
                    # print(valves[x], valves[curr_location])
                    new_minutes_you = i + real_adj[valves[x]][valves[curr_location]] + 1
                    new_minutes_elephant = i + real_adj[valves[y]][valves[elephant_location]] + 1
                    new_value = value + (26 - new_minutes_you) * flow[valves[x]] + (26 - new_minutes_elephant) * flow[valves[y]]
                    if new_minutes_you <= 26 and new_minutes_elephant <= 26:
                        dp[new_minutes_you][new_minutes_elephant][j ^ (1 << x) ^ (1 << y)] = max(dp[new_minutes_you][new_minutes_elephant][j ^ (1 << x) ^ (1 << y)] , (new_value, x, y))

print(max(collapse(dp)))