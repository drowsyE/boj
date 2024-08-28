# prefix sum
# two-pointer

import sys
input = sys.stdin.readline

N,S = map(int,input().split())
nums = [0] + list(map(int,input().split()))
sumList = [nums[0]]
for i in range(1,len(nums)):
    sumList.append(sumList[-1] + nums[i])


s=0
e=1
len_set = set()
while True:
    while True:
        total = sumList[e] - sumList[s]
        if total >= S:
            len_set.add(e-s)
            break
        e += 1
        if e == N:
            break

    while True:
        total = sumList[e] - sumList[s]
        if total < S:
            break
        len_set.add(e-s)
        s += 1
    
    if e == N:
        break

if len(len_set) == 0:
    print(0)
else:
    print(min(len_set))
