#minimum spanning tree, MST
# 14950 정복자

import sys
input = sys.stdin.readline

N,M,T = map(int,input().split())

edges = []
for _ in range(M):
    edges.append(tuple(map(int,input().split())))
edges.sort(key = lambda x : -x[2])

parent = [i for i in range(N+1)]

#union - find
def find(x):
    if x == parent[x]:
        return x
    else:
        parent[x] = find(parent[x]) # 경로 압축 
        return parent[x]
    
def union(x, y):
    x = find(x)
    y = find(y)
    if x > y:
        parent[x] = y
    elif x < y:
        parent[y] = x

#MST
w = 0
edgeCnt = 0
total_w = 0

while edgeCnt < N-1: # tree를 구성해야 되므로 간선의 개수는 전체 노드의 -1 개
    a,b,cost = edges.pop()
    if find(a) != find(b):
        union(a,b)
        total_w += (w + cost)
        w += T
        edgeCnt += 1

print(total_w)


###
#10021 watering the fields

import sys
import heapq as hq
input = sys.stdin.readline

n,c = map(int,input().split())

def dist(p1,p2): # p1 -> (x,y,idx) return -> (dist,idx1,idx2)
    return (p1[0] - p2[0])**2 + (p1[1] - p2[1])**2, p1[2], p2[2]

pos = []
for i in range(1,n+1):
    x,y = map(int,input().split())
    pos.append((x,y,i))

edges = [] # itertools combination -> 시간 오래걸림 
for i in range(n-1):
    for j in range(i+1,n):
        tmp = dist(pos[i],pos[j])
        if tmp[0] >= c: # heappop -> 시간 오래 걸림, 미리 빼주기
            hq.heappush(edges,tmp)

parent = [i for i in range(n+1)]

def find(x):
    if x == parent[x]:
        return x 
    else:
        parent[x] = find(parent[x])
        return parent[x]
    
def union(x,y):
    x = find(x)
    y = find(y)
    if x != y:
        if x > y:
            parent[x] = y
        else:
            parent[y] = x

#mst
edgeCnt = 0
total = 0
while edgeCnt < n - 1:
    try:
        w,a,b = hq.heappop(edges)
        if find(a) != find(b):
            union(a,b)
            total += w
            edgeCnt += 1
    except IndexError:
        print(-1)
        quit()

if edgeCnt != n - 1:
    print(-1)
else:
    print(total)            