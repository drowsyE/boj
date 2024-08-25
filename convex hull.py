# https://johoonday.tistory.com/205 
# 단계별 시각화 사이트

import sys
input = sys.stdin.readline

def ccw(p0, p1, p2) -> bool:
    x1, y1 = p1[0] - p0[0], p1[1] - p0[1]
    x2, y2 = p2[0] - p1[0], p2[1] - p1[1]
    return x1*y2 - y1*x2 > 0

def convex_hull(points):
    stack = []
    for p2 in points:
        while len(stack) >= 2:
            p0, p1 = stack[-2], stack[-1]
            if ccw(p0, p1, p2):
                break
            stack.pop()
        stack.append(p2)
    return len(stack)

N = int(input())
point = [tuple(map(int,input().split())) for _ in range(N)]
point.sort(key = lambda x : (x[0], x[1]))

print(convex_hull(point) + convex_hull(point[::-1]) - 2)

# 위처럼 하는 이유 -> 그라함 스캔 안씀(각도 정렬 후 스캔) 
# 따라서 모든 점을 돌았을 떄 한쪽 껍질만 나옴
# 즉 컨벡스헐 2번 해줘야됨 (정렬된 순서 + 반대로 정렬된 순서)
# -2 해주는 이유 : 컨벡스 헐 2번의 시작점과 끝점이 겹침 (시작점 = 끝점, 끝점 = 시작점)
# 이해 안되면 그려보면서 이해해보자
# 1 1
# 1 2
# 1 3
# 2 1
# 2 2
# 2 3
# 3 1
# 3 2