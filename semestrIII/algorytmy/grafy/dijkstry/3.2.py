import numpy as np
from heapq import heappush, heappop
graph = np.array([
    [0, 3, 0, 3, 5],
    [3, 0, 5, 1, 0],
    [0, 5, 0, 2, 0],
    [3, 1, 2, 0, 1],
    [5, 0, 0, 1, 0]
    ])
pred = np.full(len(graph), -1)
dist = np.full(len(graph), np.inf)
s = 0
dist[s] = 0
Q = []
for index, value in enumerate(dist):
    heappush(Q, (value, index))
nodes = [x[1] for x in Q]
while Q:
    v = heappop(Q)[1]
    nodes.remove(v)
    for i in range(len(graph)):
        if (w := graph[v][i]):
            if (d := dist[v]+w) < dist[i]:
                pred[i] = v
                dist[i] = d
print(f"pred: {[x+1 for x in pred]}")
print(f"dist: {dist}")