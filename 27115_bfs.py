# 어려웠던 문제.. bfs지만 중복 연산을 피해야되고 시간이 정말 빡빡했음
# naive한 풀이 -> O(NMK)
# p 크기대로 정렬 후 bfs -> O(NM + KlogK)
# 무지성 스위핑하면 허탈스러울 정도로 잘 풀린다.. (그래도 대회 현장이였으면 시도도 못 할듯)

from sys import stdin
from collections import deque
input = stdin.readline

dy = [1,0,-1,0]
dx = [0,1,0,-1]

N,M,K = map(int,input().split())
v = [[False] * (M+1) for _ in range(N+1)]

com = []
for _ in range(K):
    com.append(tuple(map(int,input().split())))

com.sort(key = lambda x : x[2])

q = deque()
tmp = com[-1][2]
cnt = 0
while com and com[-1][2] == tmp:
    y,x,p = com.pop()
    v[y][x] = True
    cnt += 1
    q.append((y,x,p))

while q:
    for _ in range(len(q)):
        y,x,p = q.popleft()
        if p == 0:
            continue
        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]
            if 0 < ny <= N and 0 < nx <= M:
                if not v[ny][nx]:
                    v[ny][nx] = True
                    q.append((ny,nx,p-1))
                    cnt += 1
    tmp = p-1
    while len(com) > 0 and tmp == com[-1][2]:
        y,x,p = com.pop()
        if not v[y][x]:
            v[y][x] = True
            cnt += 1
            q.append((y,x,p))
print(cnt)
