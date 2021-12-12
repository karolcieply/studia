import numpy as np
from heapq import heapify, heappush, heappop
graph = np.array([
    [0, 3, 0, 3, 5],
    [3, 0, 5, 1, 0],
    [0, 5, 0, 2, 0],
    [3, 1, 2, 0, 1],
    [5, 0, 0, 1, 0]
    ])
pred = np.full(len(graph), -1)
k = np.full(len(graph), np.inf)
# s = randint(0, len(graph)-1)
# wierzchołki numerowane od 9
s = 0
k[s] = 0
pq = []

for index, value in enumerate(k):
    heappush(pq, (value, index))
nodes = [x[1] for x in pq]
while pq:
    u = heappop(pq)[1]
    nodes.remove(u)
    for v in nodes:
        if graph[u][v] and (w := graph[u][v]) < k[v]:
            pred[v] = u
            k[v] = w
            pq[nodes.index(v)] = (k[v], v)
            heapify(pq)
print(f"pred: {[x+1 if x!=np.inf else 0 for x in pred]}")
print(f"k: {k}")
print(f"Koszt zbudowania drzewa: {sum(k)}")
