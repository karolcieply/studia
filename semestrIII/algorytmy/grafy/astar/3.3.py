import numpy as np

from heapq import heappush, heappop, heapify
graph = [
    [0,5,0,1,0,0,0,0],
    [0,0,2,0,1,0,0,0],
    [0,0,0,0,0,0,0,3],
    [0,0,0,0,1,2,0,0],
    [0,0,4,0,0,0,0,0],
    [4,0,0,0,0,0,2,0],
    [0,0,0,0,1,0,0,1],
    [0,0,0,0,2,0,0,0]
    ]

h = [4,8,3,4,5,2,1,0]


u = 0
p=0
cost = 0
S = []
Q = []
nodes = []
g = []
heappush(Q,(h[p],p))
nodes.append(p)
pred = [-1 for x in graph]
while Q:
    x = heappop(Q)
    if u:
        cost += graph[u][x[1]]
    u = x[1]
    nodes.remove(u)
    S.append(u)
    for i in range(len(graph)):
        if graph[u][i]>0:
            if (i not in S) and (i not in nodes):
                heappush(Q,(graph[u][i]+h[i]+cost, i))
                heapify(Q)
                g.append(graph[u][i]+cost)
                nodes.append(i)
                pred[i]=u
    if u+1==len(graph):
        break
print(f"{[0 if x<0 else x+1 for x in pred]}")
print(f"{[0 if x<0 else x+1 for x in S]}")