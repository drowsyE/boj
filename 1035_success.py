# 단순 완전 탐색(브루트포스) + BFS면 시간 초과가 남..
# board의 크기기ㅏ 5x5로 고정되어 있으니 비트마스킹 사용(빠름)

import sys
from collections import deque
from itertools import permutations, combinations
input = sys.stdin.readline

dy = [1,0,-1,0]
dx = [0,1,0,-1]

board = []
pos = []
for i in range(5):
    tmp = input().rstrip()
    board.append(tmp)
    for j in range(5):
        if tmp[j] == '*':
            pos.append((i,j)) # (y,x)

piece = len(pos)
if piece == 1:
    print(0)
    exit()

def check_connectivity(y,x):
    queue = deque()
    queue.append((y,x))
    visited = [0b00000 for _ in range(5)]
    board_next = [0b00000 for _ in range(5)]
    visited[y] |= (1 << x)
    for y,x in pos_next:
        board_next[y] |= (1 << x)
    while queue:
        y,x = queue.popleft()
        for i in range(4):
            ny ,nx = y + dy[i], x + dx[i]
            if 0 <= ny < 5 and 0 <= nx < 5:
                if board_next[ny] & (1 << nx) != 0 and visited[ny] & (1 << nx) == 0:
                    visited[ny] |= (1 << nx)
                    queue.append((ny,nx))

    for y,x in pos_next:
        if visited[y] & (1 << x) == 0:
            return False
    return True

MIN = 10e4
for comb in combinations(range(25),piece):
    pos_next = []
    for i in range(piece):
        pos_next.append((comb[i]//5,comb[i]%5)) # idx to coord
    if check_connectivity(pos_next[-1][0],pos_next[-1][1]):
        for perm in permutations(pos_next, piece):
            MIN = min(MIN,sum(abs(pos[i][0]-perm[i][0]) + abs(pos[i][1]-perm[i][1]) for i in range(piece)))
print(MIN)
