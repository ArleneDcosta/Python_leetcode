from typing import List
import sys

def longestlinenooptimized(M):
    if not M:
        return 0
    m = len(M)
    n = len(M[0])

    dp = [[(0,0,0,0)] * (n + 2) for _ in range(m+1)]

    ans = 0
    print(dp)
    for i in range(1,m+1):
        for j in range(1,n+1):
            if M[i-1][j-1] == 1:
                dp[i][j] = (dp[i][j-1][0] + 1 , dp[i-1][j-1][1] + 1, dp[i-1][j][2] + 1 , dp[i-1][j+1][3] + 1)
                ans = max(ans,max(dp[i][j]))
    return ans

def longest_line_optimized(M):
    if not M:
        return 0
    
    m, n = len(M), len(M[0])
    
    prev = [(0, 0, 0, 0)] * (n + 2)  
    ans = 0

    for i in range(m):
        curr = [(0, 0, 0, 0)] * (n + 2) 
        for j in range(1, n + 1):
            if M[i][j - 1] == 1:
                curr[j] = (
                    curr[j - 1][0] + 1,  
                    prev[j - 1][1] + 1,  
                    prev[j][2] + 1,      
                    prev[j + 1][3] + 1  
                )
                ans = max(ans, max(curr[j]))

        prev = curr  # Move to the next row

    return ans


def longestlineno(matrix):
    r = len(matrix)
    c = len(matrix[0])

    def checkrowcount(cnt, i,j):
        if i >= r or matrix[i][j] == 0:
            return cnt
        
        if matrix[i][j] == 1:
            cnt += 1 
        cnt = checkrowcount(cnt,i+1,j)
        return cnt
    
    def checkcolcount(cnt,i,j):
        if j >= c or matrix[i][j] == 0:
            return cnt
        if matrix[i][j] == 1:
            cnt += 1 
        cnt = checkcolcount(cnt,i,j+1)
        return cnt
        
    def checkdcount(cnt,i,j):
        if j >= c or i >= r or matrix[i][j] == 0:
            return cnt
        if matrix[i][j] == 1:
            cnt += 1 
        cnt = checkdcount(cnt,i+1,j+1)
        return cnt
        

    finalres = 0
    for i in range(0,r):
        for j in range(0,c):
            if matrix[i][j] == 1:
                finalres = max(finalres,checkrowcount(0,i,j))
                finalres = max(finalres,checkcolcount(0,i,j))
                finalres = max(finalres,checkdcount(0,i,j))
                if finalres >= r - i or finalres >= c - j:
                    return finalres
    return finalres


if __name__ == '__main__':
    print(longestlinenooptimized([[0,1,1,0],[0,1,0,0],[0,0,0,1]]))
