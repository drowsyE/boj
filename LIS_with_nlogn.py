# 12015 가장 긴 증가하는 부분 수열 2 / 골드 2

#   원리 설명 :
#   seq = [10, 20, 30, 15, 50] 이라 가정
#   핵심은 길이는 LIS 이지만 원소는 LIS를 구성하지 않음!
#   1. 우선 seq[0]을 LIS에 담음 -> LIS = [10]
#   2. 앞에서부터 LIS[-1]보다 크면 원소를 담음 -> LIS[10, 20]
#   3. LIS[-1] = 20 > seq[3] = 15 임으로 LIS에서 이분탐색을 하여 15보다 큰 처음로 등장하는 원소를 탐색함 -> 20
#   4. 그 원소를 15로 바꿈 = 20 -> 15
#   5. 위 과정을 반복해서 나온 LIS = [10, 15, 30 ,50]
#                     진짜 LIS는 [10, 20, 30, 50], but 길이는 진짜 LIS와 같음
#
#   3,4 의 과정을 하는 이유 ->  '가능성이 있는 원소로 바꾼다'로 생각하면 됨
#   최대한 작은 원소들로 바꿈으로써 최대한 긴 수열을 만들려고 하기 때문
#   모든 원소가 대체되기 전까지는 대체 전 원소로 기능을 하고 대체 원소를 포함해서 LIS의 원소들의 seq에서의 인덱스가 오름차순이면 그때 대체 원소가 제 기능을 함
#   즉, 20을 15로 바꿔도 15는 20의 역할을 함
#      
#   LIS = [10, 15(사실상 20), 30]에서
#   만약 다음 원소로 10보다 크고 15보다 작은 원소가 온다 -> 15를 대체(그래도 20의 역할을 함)
#   만약 다음 원소로 15보다 크고 30보다 작은 원소가 온다 ex) 25 -> 30을 대체함으로써 
#       LIS = [10, 15, 25]가 되고 15와 25는 자신의 기능을 함
#
#
#   이해가 안된다면 seq = [10, 20, 30, 15, 25, 27] 일 때의 과정을 직접 풀어보자   


import sys
input = sys.stdin.readline

N = int(input())
seq = list(map(int,input().split()))
LIS = [seq[0]]


def binary_search(x):
    start = 0
    end = len(LIS) - 1
    while start <= end:
        mid = (start + end) // 2

        if LIS[mid] < x:
            start = mid + 1
        elif LIS[mid] > x:
            end = mid - 1
        else:
            return mid
    return start

for num in seq:
    if num > LIS[-1]:
        LIS.append(num)
    elif num < LIS[-1]:
        LIS[binary_search(num)] = num

print(len(LIS))