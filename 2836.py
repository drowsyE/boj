# sweeping

from sys import stdin
input = stdin.readline
N,M = map(int,input().split())
tmp = []
for _ in range(N):
    a,b = map(int,input().split())
    if a > b:
        tmp.append((b,a))
tmp.sort(key = lambda x : -x[0])
s,e = tmp.pop()
while tmp:
    a,b = tmp.pop()
    if a <= e < b:
        e = b
    elif e < a:
        M += (e-s)*2
        s,e = a,b
M += (e-s)*2
print(M)
