# 검색 엔진 - P3
# SCC, Topology sort, Hashing
# Hello P5!

from sys import stdin
from collections import deque
input = stdin.readline

N = int(input())
idx_ = 0
idx = {}

query = []
# str to int (starts from 0)
for _ in range(N):
    tmp = input().rstrip().split()
    query.append(tmp)
    for i in range(len(tmp)):
        if i == 1:
            continue

        if idx.get(tmp[i],-1) == -1:
            idx[tmp[i]] = idx_
            idx_ += 1

# make graph
graph = [set() for _ in range(idx_)]
indegree = [0] * idx_
for q in query:
    e = idx[q[0]]
    indegree[e] += int(q[1])
    for i in range(2,2+int(q[1])):
        graph[idx[q[i]]].add(e)

id = -1
parent = [-1] * idx_
stack = []
sccs = []
inStack = [False] * idx_

def dfs(cur):
    global id
    id += 1
    parent[cur] = id
    stack.append(cur)
    inStack[cur] = True

    p = parent[cur]
    for next in graph[cur]:
        if parent[next] == -1:
            p = min(p,dfs(next))
        elif inStack[next]:
            p = min(p,parent[next])

    if p == parent[cur]:
        scc = []
        while True: 
            node = stack.pop()
            inStack[node] = False
            scc.append(node)
            if cur == node:
                break
        sccs.append(scc)
    return p

for i in range(idx_):
    if parent[i] == -1:
        dfs(i)

# disconnect edges
for scc in sccs:
    if len(scc) == 1:
        continue
    for i in range(len(scc)):
        now = scc[i]
        for j in range(len(scc)):
            if i == j:
                pass
            if scc[j] in graph[now]:
                graph[now].remove(scc[j])
                indegree[scc[j]] -= 1

q = deque()
for i in range(idx_):
    if indegree[i] == 0:
        q.append(i)

point = [1] * idx_
while q:
    now = q.popleft()
    for next in graph[now]:
        point[next] += point[now]
        indegree[next] -= 1
        if indegree[next] == 0:
            q.append(next)

print(point[idx[input().rstrip()]])
