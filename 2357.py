# segment tree

import sys
input = sys.stdin.readline

N,M = map(int,input().split())

leafCnt = 1
while leafCnt <= N:
    leafCnt <<= 1

segTree = [(1e9+1,0)] * ((leafCnt<<1)+1) #(MIN,MAX)
for i in range(N):
    tmp = int(input())
    segTree[leafCnt+i] = (tmp,tmp)

#initialize tree
for i in range(leafCnt-1,0,-1):
    segTree[i] = (min(segTree[i*2][0],segTree[i*2+1][0]),max(segTree[i*2][1],segTree[i*2+1][1]))

def getMinMax(s,e):
    MIN, MAX = 1e9+1, 0
    while s <= e:
        if s%2 == 1:
            MIN = min(MIN,segTree[s][0])
            MAX = max(MAX,segTree[s][1])
            s += 1
        if e%2 == 0:
            MIN = min(MIN,segTree[e][0])
            MAX = max(MAX,segTree[e][1])
            e -= 1
        s//=2
        e//=2
    print(MIN,MAX)

for _ in range(M):
    a,b = map(int,input().split())
    getMinMax(leafCnt-1+a,leafCnt-1+b)
