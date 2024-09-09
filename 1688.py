#  Ray Casting 알고리즘
# 다각형 내의 점 판별

from sys import stdin
input = stdin.readline

def ccw(p1,p2,p3):
    x1, y1 = p2[0] - p1[0], p2[1] - p1[1]
    x2, y2 = p3[0] - p2[0], p3[1] - p2[1]
    res = x1*y2 - x2*y1
    if res > 0:
        return 1
    elif res < 0:
        return -1
    else:
        return 0

def isIntersect(p1,p2,p3,p4):
    abc = ccw(p1,p2,p3)
    abd = ccw(p1,p2,p4)
    cda = ccw(p3,p4,p1)
    cdb = ccw(p3,p4,p2)
    if abc * abd <= 0 and cda * cdb <= 0:
        return 1
    else:
        return 0

N  = int(input())
p = [tuple(map(int,input().split())) for _ in range(N)]
people = [tuple(map(int,input().split())) for _ in range(3)]

for j in range(3):
    cnt = 0
    flg = False
    for i in range(-1,len(p)-1):
        if ccw(p[i],p[i+1],people[j]) != 0:
            cnt += isIntersect(people[j],(people[j][0]+1,people[j][1]+100000007),p[i],p[i+1])
        else:
            if min(p[i][0],p[i+1][0]) <= people[j][0] <= max(p[i][0],p[i+1][0]) and\
             min(p[i][1],p[i+1][1]) <= people[j][1] <= max(p[i][1],p[i+1][1]):
                flg = True
                break
    if flg or cnt % 2:
        print(1)
    else:
        print(0)
