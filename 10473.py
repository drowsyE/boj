# 유익한 문제 
# 기하학, 데이크스트라 or 플로이드-워셜 / 기하학 + 최단경로**
# 간선의 방향이 주어지지 않아도 데이크스트라를 쓸 수 있다!

# 대포를 기준으로
# 거리가 30m 이하 -> 걷는게 유리
# 거리가 30m 이상 -> 대포가 유리

import sys
import heapq as hq
from math import sqrt
input = sys.stdin.readline

def dist(x1,y1,x2,y2):
    return sqrt((x1-x2)**2 + (y1-y2)**2)

node = []
node.append(tuple(map(float,input().split())))
ex, ey = map(float,input().split())
n = int(input())
for _ in range(n):
    node.append(tuple(map(float,input().split())))
node.append((ex,ey))

time = [0 for _ in range(n+2)] # 0 -> start, n+1 -> end
visited = [False for _ in range(n+2)]

heapq = []
visited[0] = True
for i in range(1,n+2):
    tmp = dist(node[0][0],node[0][1],node[i][0],node[i][1])/5
    heapq.append((tmp,i))
    time[i] = tmp
hq.heapify(heapq)

while heapq: # (time, node)
    nowT, nowN = hq.heappop(heapq)
    if nowN == n+1:
        break
    if visited[nowN]:
        continue
    visited[nowN] = True
    for i in range(1,n+2):
        if visited[i] != True:
            tmp = dist(node[nowN][0],node[nowN][1],node[i][0],node[i][1])
            if tmp > 30:
                res = time[nowN] +2 +abs(tmp-50)/5 # +2 +|tmp-50|/5
                if time[i] > res: 
                    time[i] = res
                    hq.heappush(heapq,(time[i],i))
            else:
                res = time[nowN] + tmp/5
                if time[i] > res:
                    time[i] = res
                    hq.heappush(heapq,(time[i],i))
                    
print(round(time[n+1],7))
