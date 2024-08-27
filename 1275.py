# segment tree

import sys
input = sys.stdin.readline

N,Q = map(int,input().split())
nums = tuple(map(int,input().split()))

leafCnt = 1
while leafCnt <= N:
    leafCnt <<= 1

segTree = [0] * ((leafCnt<<1)+1)
for i in range(N):
    segTree[leafCnt+i] = nums[i]

for i in range((leafCnt<<1)-1,0,-1):
    segTree[i//2] += segTree[i]

def getSum(s,e):
    total = 0
    while s <= e:
        if s%2 == 1:
            total += segTree[s]
            s += 1
        if e%2 == 0:
            total += segTree[e]
            e -= 1
        s //= 2
        e //= 2
    return total

def changeVal(idx, v):
    d = v - segTree[idx]
    while idx != 0:
        segTree[idx] += d
        idx //= 2

for _ in range(Q):
    x,y,a,b = map(int,input().split())
    if x > y:
        x,y, = y,x
    print(getSum(leafCnt-1+x,leafCnt-1+y))
    changeVal(leafCnt-1+a,b)
