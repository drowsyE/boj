# Segment Tree -> 구간에 대한 처리 ex) 구간 합, 최대, 최소
# seqidx2segTreeidx -> (segTree idx, 1부터) = (seq idx, 1부터) + 2^k - 1
# leaf node의 개수 = 2^k (필수 x)

# 2042 구간 합 구하기

import sys
from math import log2, ceil
input = sys.stdin.readline

N,M,K = map(int,input().split())

k = ceil(log2(N)) # k = tree height
nodeCnt = 2**(k+1)


segTree = [0] * nodeCnt
nodeStartLeft = nodeCnt//2
for i in range(N):
    segTree[nodeStartLeft + i] = int(input())

# initialize tree
i = nodeCnt - 1
while i != 1:
    segTree[i//2] += segTree[i]
    i -=1

def changeVal(idx, value):
    d = value - segTree[idx]
    while idx != 0:
        segTree[idx] += d
        idx //= 2

def getSum(start, end):
    total = 0
    while start <= end:
        if start % 2 == 1:
            total += segTree[start]
            start += 1
        if end % 2 == 0:
            total += segTree[end]
            end -= 1
        start //= 2
        end //= 2
    return total

for _ in range(M+K):
    q,a,b = map(int,input().split())

    if q == 1:
        changeVal(nodeStartLeft-1+a, b)
    else:
        print(getSum(nodeStartLeft-1+a,nodeStartLeft-1+b))