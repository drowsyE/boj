# TIME OUT

import sys
from collections import deque
from itertools import permutations
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
    visited = [[False for _ in range(5)] for _ in range(5)]
    board_next = [[False for _ in range(5)] for _ in range(5)]
    visited[y][x] = True
    for y,x in pos_next:
        board_next[y][x] = True
    while queue:
        y,x = queue.popleft()
        for i in range(4):
            ny ,nx = y + dy[i], x + dx[i]
            if 0 <= ny < 5 and 0 <= nx < 5:
                if board_next[ny][nx] and not visited[ny][nx]:
                    visited[ny][nx] = True
                    queue.append((ny,nx))

    for y,x in pos_next:
        if not visited[y][x]:
            return False
    return True

MIN = 10e4
for perm in permutations(range(25),piece):
    pos_next = []
    for i in range(piece):
        pos_next.append((perm[i]//5,perm[i]%5)) # idx to coord
    if check_connectivity(pos_next[-1][0],pos_next[-1][1]):
        MIN = min(MIN,sum(abs(pos[i][0]-pos_next[i][0]) + abs(pos[i][1]-pos_next[i][1]) for i in range(piece)))
print(MIN)
