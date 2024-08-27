#bfs

from collections import deque

N,K = map(int,input().split())

q = deque()
q.append((N,0))
visited = [False] * 100001
visited[N] = True
while True:
    n,step = q.popleft()
    if n == K:
        print(step)
        break
    for next in [n-1,n+1,n*2]:
        if 0 <= next < 100001 and not visited[next]:
            visited[next] = True
            q.append((next,step+1))
