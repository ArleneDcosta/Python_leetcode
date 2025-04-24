
from collections import Counter

def minInsertions(s: str) -> int:
    n = len(s)
    dp = [[0] * (n + 1) for i in range(n + 1)]
    for i in range(n):
        for j in range(n):
            print(i,j,~j)
            dp[i + 1][j + 1] = dp[i][j] + 1 if s[i] == s[~j] else max(dp[i][j + 1], dp[i + 1][j])
            print( dp[i + 1][j + 1])
    print(dp)
    return n - dp[n][n]

'''The no will increase when the subsequent element is a palindrome or has similiar element else its different so will not
increase and the no will remain the same'''

if __name__ == '__main__':
    # print(minInsertions(s = "zzazz"))
    # print(minInsertions(s = "zjveiiwvc"))
    print(minInsertions(s = "le"))
