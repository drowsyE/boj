# 25307
# 시간 매우 빡빡함, 구현을 완벽하게 해야된다는 교훈을 얻음(불필요하다고 생각하는 것도 구현해 볼 것)
# boolean를 다루는 것이 빠르다는것을 알았음

import sys
from collections import deque
input = sys.stdin.readline

dy = [1,0,-1,0]
dx = [0,1,0,-1]

N,M,K = map(int,input().split())
m = []
danger = [[False for _ in range(M)] for _ in range(N)]
visited = [[False for _ in range(M)] for _ in range(N)]
queue = deque()

for i in range(N):
    tmp = list(map(int,input().split()))
    m.append(tmp)
    for j in range(M):
        if tmp[j] == 4:
            start = (i,j,0) # y,x,step
        elif tmp[j] == 3:
            queue.append((i,j,0))
            danger[i][j] = True
    
def move_manekin(queue,K): # 한번에 병렬적으로
    while queue:
        y,x,step = queue.popleft()
        if step == K:
            continue
        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]
            if 0 <= ny < N and 0 <= nx < M:
                if not danger[ny][nx]:
                    danger[ny][nx] = True
                    queue.append((ny,nx,step+1))

def move(p):
    queue = deque()
    queue.append(p)
    visited[p[0]][p[1]] = True
    while queue:
        y,x,step = queue.popleft()
        if m[y][x] == 2:
            return step
        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]
            if 0 <= ny < N and 0 <= nx < M:
                if not visited[ny][nx] and not danger[ny][nx] and not m[ny][nx] == 1:
                    visited[ny][nx] = True
                    queue.append((ny,nx,step+1))
    return -1

if K != 0:
    move_manekin(queue,K)

print(move(start))
