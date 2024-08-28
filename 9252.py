# LCS

import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

def dfs(y,x,l,lcs:list): #그냥 반복문으로 찾아도 됨
    if len(lcs) == l:
        return lcs
    if LCS[y-1][x] == LCS[y][x]:
        return dfs(y-1,x,l,lcs)
    elif LCS[y][x-1] == LCS[y][x]:
        return dfs(y,x-1,l,lcs)
    else:
        lcs.append(str1[x])
        return dfs(y-1,x-1,l,lcs)
    

str1 = '_' + input().rstrip()
str2 = '_' + input().rstrip()

LCS = [[0 for _ in range(len(str1))] for _ in range(len(str2))]

for i in range(1,len(str2)):
    for j in range(1,len(str1)):
        if str1[j] == str2[i]:
            LCS[i][j] = LCS[i-1][j-1] + 1
        else:
            LCS[i][j] = max(LCS[i-1][j],LCS[i][j-1])

print(LCS[-1][-1])
if LCS[-1][-1] > 0:
    lcs = dfs(len(str2)-1,len(str1)-1,LCS[-1][-1],[])
    print(''.join(lcs[::-1]))
