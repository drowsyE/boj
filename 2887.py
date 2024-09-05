# 감각적 직관으로 한번에 맞춘 문제!
# plat 5 / 행성 터널
# mst, sort

from sys import stdin
input = stdin.readline

def find(x):
    if x != parent[x]:
        parent[x] = find(parent[x])
    return parent[x]
    

def union(x,y):
    x = find(x)
    y = find(y)
    if x > y:
        parent[x] = y
    else:
        parent[y] = x
    

N = int(input())
parent = [i for i in range(N)]
x = []
y = []
z = []
for i in range(N):
    x_,y_,z_ = map(int,input().split())
    x.append((x_,i))
    y.append((y_,i))
    z.append((z_,i))

x.sort()
y.sort()
z.sort()

edges = []
for i in range(N-1):
    x1,i1 = x[i]
    x2,i2 = x[i+1]
    edges.append((i1,i2,x2-x1))
    y1,i1 = y[i]
    y2,i2 = y[i+1]
    edges.append((i1,i2,y2-y1))
    z1,i1 = z[i]
    z2,i2 = z[i+1]
    edges.append((i1,i2,z2-z1))



edges.sort(key=lambda x : x[2])
# MST
nodeCnt = 0
total = 0
for a,b,w in edges: # (a,b,w)
    if find(a) != find(b):
        union(a,b)
        total += w
        nodeCnt += 1

        if nodeCnt == N-1:
            break
print(total)
