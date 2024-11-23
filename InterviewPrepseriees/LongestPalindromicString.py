def longestPalindrome(s: str) -> str:
    dp = [[0 for i in range(0, len(s))] for y in range(0, len(s))]
    lengthstr = 1
    resultstr = ''
    for i in range(0, len(s)):
        dp[i][i] = 1
        resultstr = s[i:i + 1]

    for i in range(0, len(s) - 1):
        if s[i] == s[i + 1]:
            dp[i][i + 1] = 2
            if dp[i][i + 1] > lengthstr:
                lengthstr = dp[i][i + 1]
                resultstr = s[i:i + 2]

    for st in range(3, len(s) + 1):
        for start in range(0, len(s) - st + 1):
            end = start + st - 1
            if s[start] == s[end] and dp[start + 1][end - 1] != 0:
                dp[start][end] = dp[start + 1][end - 1] + 2
                if dp[start][end] > lengthstr:
                    lengthstr = dp[start][end]
                    resultstr = s[start:end + 1]
    print(dp)
    return resultstr

if __name__ == '__main__':
    print(longestPalindrome("babad"))