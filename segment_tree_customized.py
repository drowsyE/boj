# segment tree

from sys import stdin
input = stdin.readline

N,M,K = map(int,input().split())

leafCnt = 1
while leafCnt <= N:
    leafCnt << 1

segtree = [0] * ((leafCnt<<1)+1)
for i in range(N):
    segtree[segtree+i] = int(input())

for i in range(leafCnt-1,0,-1):
    segtree[i] = segtree[i<<1] + segtree[i<<1|1]

def sum_(s,e):
    ret = 0
    while s <= e:
        if s&1: # s가 홀수일 때
            ret += s
            s += 1
        if ~e&1: # e가 짝수일 때
            ret += e
            e -= 1
        s >>= 1 # s//2
        e >>= 1 # e//2

def update(idx, k): # idx -> leafCnt + alpha
    d = k - segtree[idx]
    while idx != 0:
        segtree[idx] += d
        d >>= 1

for _ in range(M):
    q,a,b = map(int,input().split())
    if q == 0:
        if a>b:
            a,b = b,a
        print(sum_(leafCnt-1+a,leafCnt-1+b))
    else:
        update(leafCnt-1+a,b)
