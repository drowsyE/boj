# implementation, simulation
from 삼성 SW 역량 테스트 기출 문제 / https://www.acmicpc.net/workbook/view/1152


import sys
input = sys.stdin.readline

N,M,y,x,K = map(int,input().split())
m = [list(map(int,input().split())) for _ in range(N)]
dice = [0 for _ in range(7)] # 1이 윗면, 6이 밑면

def rotate(i):
    global x,y
    flg = False
    if i == 1 and x + 1 < M:
        dice[1],dice[3],dice[4],dice[6] = \
        dice[4],dice[1],dice[6],dice[3]
        x += 1
        flg = True

    elif i == 2 and x > 0:
        dice[1],dice[3],dice[4],dice[6] = \
        dice[3],dice[6],dice[1],dice[4]
        x -= 1
        flg = True

    elif i == 3 and y > 0:
        dice[1],dice[2],dice[5],dice[6] = \
        dice[5],dice[1],dice[6],dice[2]
        y -= 1
        flg = True

    elif i == 4 and y + 1 < N:
        dice[1],dice[2],dice[5],dice[6] = \
        dice[2],dice[6],dice[1],dice[5]
        y += 1
        flg = True
    
    if not flg:
        return False
    return True

for q in map(int,input().split()):
    if not rotate(q):
        continue
    if m[y][x] == 0:
        m[y][x] = dice[6]
    else:
        dice[6] = m[y][x]
        m[y][x] = 0
    print(dice[1])
