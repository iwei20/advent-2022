from collections import defaultdict

stay_white_condition = True
turn_white_condition = True

iterations = 5
current = []
adj = defaultdict()
for i in range(iterations):
    next = []
    for node in current:
        if stay_white_condition:
            next.append(node)

        for adj_node in adj[node]:
            if turn_white_condition:
                next.append(adj_node)

    current = next
