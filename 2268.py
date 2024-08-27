# segment tree

import sys
input = sys.stdin.readline

N,M = map(int,input().split())

leafCnt = 1
while leafCnt <= N:
    leafCnt <<= 1

segTree = [0] * (leafCnt<<1)

def sum_(s,e):
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

def modify_(i,k):
    d = k - segTree[i]
    while i != 0:
        segTree[i] += d
        i //= 2

for _ in range(M):
    q,a,b = map(int,input().split())
    if q == 0:
        if a>b:
            a,b = b,a
        print(sum_(leafCnt-1+a,leafCnt-1+b))
    else:
        modify_(leafCnt-1+a,b)
