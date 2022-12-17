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

for line in lines:
    line = line.replace("tunnel ", "tunnels ")
    line = line.replace("valve ", "valves ")
    line = line.replace("lead ", "leads ")
    r = pattern.parse(line)

    flow[r[0]] = r[1]
    adj[r[0]] = list(r[2].split(", "))

# (benefit, name, new_minutes)
def select_next(location, minutes_so_far):
    global adj, flow, opened
    costs = []
    visited = defaultdict(bool)
    bfs = deque()
    bfs.append((flow[location] * (29 - minutes_so_far), location, minutes_so_far + 1))
    visited[location] = True
    while bfs:
        next_item = bfs.popleft()
        costs.append(next_item)
        for other in adj[next_item[1]]:
            if not visited[other]:
                bfs.append((flow[other] * (29 - next_item[2]), other, next_item[2] + 1))
                visited[other] = True

    calc = [i for i in costs if not opened[i[1]] and i[2] <= 30]
    if not calc:
        return None
    result = max(calc)
    print(result)
    return result

curr_location = "AA"
minutes = 0
pressure = 0
while minutes < 30:
    bruh = select_next(curr_location, minutes)
    if bruh is None:
        break
    total_gen, location, new_minutes = bruh
    if location == curr_location:
        pressure += total_gen
        minutes = new_minutes
        opened[location] = True

    max_bruh = (0, "AA")
    for other in adj[curr_location]:
        bruh = select_next(other, minutes + 1)
        if bruh is None:
            break
        total_gen, location, new_minutes = bruh
        max_bruh = max(max_bruh, (total_gen, other))
    curr_location = max_bruh[1]
    minutes += 1
    print(curr_location)

print(pressure)