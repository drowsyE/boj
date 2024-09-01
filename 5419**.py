# fenwick_tree(BIT) (or.. segment_tree), sweeping, coordinate compression
# 팬윅 트리, 스위핑 응용, 좌표 압축이라는 것을 배움!

from sys import stdin
input = stdin.readline

def update(i,diff):
    while i <= N:
        fen[i] += diff
        i += (i & -i)

def sum_(e):
    ret = 0
    while e > 0:
        ret += fen[e]
        e -= (e & -e)
    return ret

for _ in range(int(input())):
    N = int(input())
    land = []
    for _ in range(N):
        x, y = map(int,input().split())
        land.append((x,-y)) # y를 그대로 받으면 팬윅 트리에서 연산이 많아져서 거꾸로 받음
    fen = [0] * 75001

    land.sort(key=lambda x: x[1]) # 좌표 압축을 위해 정렬
    land_zip = [(land[0][0],1)] 
    idx = 1
    for i in range(1,len(land)):
        if land[i][1] > land[i-1][1]:
            idx += 1
        land_zip.append((land[i][0],idx))
    land_zip.sort(key= lambda x : (x[0], x[1])) # 스위핑을 위해 정렬

    ans = 0
    for x,y in land_zip:
        ans += sum_(y)
        update(y,1)

    print(ans)
