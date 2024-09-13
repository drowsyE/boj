# dijkstra
# 역추적을 해야되는 문제

from sys import stdin, maxsize
import heapq as hq
input = stdin.readline

N = int(input())
M = int(input())
graph = [[] for _ in range(N+1)]
for _ in range(M):
    a,b,w = map(int,input().split())
    graph[a].append((b,w))

dist = [maxsize] * (N+1)
parent = [i for i in range(N+1)]
visited = [False] * (N+1)

S,E = map(int,input().split())
dist[S] = 0
heap = [(0,S)]
while heap:
    now_dist, now = hq.heappop(heap)
    if now == E:
        break
    if visited[now]:
        continue
    visited[now] = True
    for next, cost in graph[now]:
        if dist[next] > now_dist + cost:
            dist[next] = now_dist + cost
            hq.heappush(heap,(dist[next],next))
            parent[next] = now

print(dist[E])

stack = [E]
while E != S:
    tmp = parent[E]
    stack.append(tmp)
    E = tmp

print(len(stack))
while stack:
    print(stack.pop(),end =' ')
