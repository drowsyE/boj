# a.k.a Binary Index Tree
# if 원소의 개수가 n개 -> 배열 크기 n+1 (1부터 인덱싱하기 떄문)
# 세그먼트 트리보다 적은 메모리를 차지함
# ex) 27 = 11011(2) 더하고 최하위 비트를 뺴는 연산 반복
# => A[27] + A[26] + A[24] + A[16]

# https://growth-coder.tistory.com/165
# https://yoongrammer.tistory.com/104
# https://youtu.be/fg2iGP4e2mc

# 2042 - 구간 합 구하기

from sys import stdin
input = stdin.readline

def update(i, num):
    diff = num - nums[i]
    while i <= N:
        fen[i] += diff
        i += (i & -i)

def sum_(s, e):
    s -= 1
    ret = 0
    while e > 0:
        ret += fen[e]
        e -= (e & -e)
    
    while s > 0:
        ret -= fen[s]
        s -= (s & -s)

    return ret

N,M,K = map(int,input().split())
fen = [0 for _ in range(N+1)]
nums = [0 for _ in range(N+1)]
for i in range(1,N+1):
    tmp = int(input())
    update(i,tmp)
    nums[i] = tmp

for _ in range(M+K):
    q,x,y = map(int,input().split())
    if q == 1:
        update(x,y)
        nums[x] = y
    else:
        print(sum_(x,y))
