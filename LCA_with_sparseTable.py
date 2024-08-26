import sys
from collections import deque
input = sys.stdin.readline

N = int(input())
tree = [[] for _ in range(N+1)]
for _ in range(N-1):
    a,b = map(int,input().split())
    tree[a].append(b)
    tree[b].append(a)

tmp = 1
kmax = 0 
while tmp <= N:
    tmp <<= 1
    kmax += 1

depth = [0 for _ in range(N+1)]
visited = [False for _ in range(N+1)]
parent = [[0 for _ in range(N+1)] for _ in range(kmax+1)] # P[K][N] = P[K-1][P[K-1][N]]
def BFS(x):
    queue = deque()
    queue.append(x)
    visited[x] = True
    while queue:
        now = queue.popleft()
        for i in tree[now]:
            if not visited[i]:
                visited[i] = True
                depth[i] = depth[now] + 1
                queue.append(i)
                parent[0][i] = now

BFS(1)
for k in range(1,kmax + 1):
    for n in range(1,N+1):
        parent[k][n] = parent[k-1][parent[k-1][n]]

def LCA(a,b):
    if depth[a] > depth[b]:
        a,b = b,a
    
    for k in range(kmax, -1, -1):
        if pow(2,k) <= depth[b] - depth[a]:
            if depth[a] <= depth[parent[k][b]]:
                b = parent[k][b]

    for k in range(kmax, -1, -1):
        if a == b:
            break
        if parent[k][a] != parent[k][b]:
            a = parent[k][a]
            b = parent[k][b]
        
    if a == b:
        return a
    else:
        return parent[0][a]

M = int(input())
for _ in range(M):
    a,b = map(int,input().split())
    print(LCA(a,b))
