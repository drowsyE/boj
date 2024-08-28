# DP, LCS
# https://velog.io/@emplam27/알고리즘-그림으로-알아보는-LCS-알고리즘-Longest-Common-Substring와-Longest-Common-Subsequence

import sys
input = sys.stdin.readline

str1 = '_' + input().rstrip()
str2 = '_' + input().rstrip()

LCS = [[0 for _ in range(len(str1))] for _ in range(len(str2))]

#LCS algorithm
for i in range(1,len(str2)):
    for j in range(1,len(str1)):
        
        if str2[i] == str1[j]:
            LCS[i][j] = LCS[i-1][j-1] + 1
        else:
            LCS[i][j] = max(LCS[i-1][j],LCS[i][j-1])

print(LCS[-1][-1])
#제일 마지막 원소는 무조건 최댓값임!

