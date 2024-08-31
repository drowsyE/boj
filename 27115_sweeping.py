# 27715 with 4 directional sweeping -> much faster than bfs

from sys import stdin
input = stdin.readline

N,M,K = map(int,input().split())
m = [[0 for _ in range(M)] for _ in range(N)]
for _ in range(K):
    y,x,p = map(int,input().split())
    m[y-1][x-1] = p+1

for i in range(N-1):
    for j in range(M):
        m[i+1][j] = max(m[i+1][j], m[i][j]-1)

for i in range(N-1,0,-1):
    for j in range(M):
        m[i-1][j] = max(m[i-1][j], m[i][j]-1)

for i in range(N):
    for j in range(M-1):
        m[i][j+1] = max(m[i][j+1], m[i][j]-1)

for i in range(N):
    for j in range(M-1,0,-1):
        m[i][j-1] = max(m[i][j-1], m[i][j]-1)

cnt = 0
for i in range(N):
    for j in range(M):
        if m[i][j]:
            cnt += 1
print(cnt)
