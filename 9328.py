# 함정이 많다
# 골드 1 - 열쇠
# bfs

from sys import stdin
from collections import deque
input = stdin.readline

dx = [1,0,-1,0]
dy = [0,1,0,-1]
ans = []
def det(ny,nx):
    global keys, cnt
    nb = building[ny][nx]
    if visited[ny][nx] or nb == '*':
        return
    
    elif nb == '$':
        cnt += 1
        visited[ny][nx] = True
        q.append((ny,nx))

    elif nb == '.':
        visited[ny][nx] = True
        q.append((ny,nx))

    elif 64 < ord(nb) < 91:
        visited[ny][nx] = True
        if keys & (1 << ord(nb) - 65):
            q.append((ny,nx))
        else:
            door_tmp.append((ny,nx))
    else:
        keys |= (1 << ord(nb) - 97)
        visited[ny][nx] = True
        q.append((ny,nx))

T = int(input())
for _ in range(T):

    cnt = 0
    keys = 0b00000000000000000000000000
    door_tmp = deque()
    q = deque()
    h,w = map(int,input().split())
    building = [input().rstrip() for _ in range(h)]
    visited = [[False] * w for _ in range(h)]

    for i in range(w):
        det(0,i)
        det(h-1,i)
    for i in range(1,h-1):
        det(i,0)
        det(i,w-1)

    tmp = input().rstrip()
    if tmp != '0':
        for key in tmp:
            keys |= (1 << ord(key) - 97)
    while True:
        while q:
            y,x = q.popleft()
            for i in range(4):
                ny, nx = y + dy[i], x + dx[i]
                if 0 <= ny < h and 0 <= nx < w:
                    det(ny,nx)

        for _ in range(len(door_tmp)):
            y,x = door_tmp.popleft()
            if keys & (1 << ord(building[y][x]) - 65):
                q.append((y,x))
            else:
                 door_tmp.append((y,x))
        
        if not q:
            break
    ans.append(cnt)
for i in ans:
    print(i)
