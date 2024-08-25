# ccw / counter clockwise
# 17387 선분 교차 2
# 꽤나 어렵기 떄문에 최대한 이해해보자
# https://gaussian37.github.io/math-algorithm-line_intersection/

import sys
input = sys.stdin.readline

x1,y1,x2,y2 = map(int,input().split()) #ab
x3,y3,x4,y4 = map(int,input().split()) #cd

def ccw(x1,y1,x2,y2,x3,y3):
    res = (x1*y2 + x2*y3 + x3*y1) - (x2*y1 + x3*y2 + x1*y3)
    if res > 0:
        return 1
    elif res < 0:
        return -1 
    else:
        return 0

def main(x1,y1,x2,y2,x3,y3,x4,y4):
    abc = ccw(x1,y1,x2,y2,x3,y3)
    abd = ccw(x1,y1,x2,y2,x4,y4)
    cda = ccw(x3,y3,x4,y4,x1,y1)
    cdb = ccw(x3,y3,x4,y4,x2,y2)

    if abc * abd == 0 and cda * cdb == 0:
        if min(x1,x2) <= max(x3,x4) and min(x3,x4) <= max(x1,x2)\
            and min(y1,y2) <= max(y3,y4) and min(y3,y4) <= max(y1,y2):
            return 1
        return 0
    elif abc * abd <= 0 and cda * cdb <= 0:
        return 1
    else:
        return 0

print(main(x1,y1,x2,y2,x3,y3,x4,y4))