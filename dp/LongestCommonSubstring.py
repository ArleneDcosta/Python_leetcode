# Python implementation of the above approach

# Function to find the length of the
# longest LCS
def LCSubStr(s, t, n, m):
    #n=len(X),#m = len(Y)
    #src taken 0 and 1 and target considered length
    # Create DP table
    dp = [[0 for j in range(m + 1)] for i in range(2)]
    print(dp)
    res = 0

    for i in range(1, n + 1):
        for j in range(1, m + 1):
            if (s[i - 1] == t[j - 1]):
                dp[i % 2][j] = dp[(i - 1) % 2][j - 1] + 1
                if (dp[i % 2][j] > res):
                    res = dp[i % 2][j]
            else:
                dp[i % 2][j] = 0

    return res


# Driver Code
X = "OldSite:GeeksforGeeks.org"
Y = "NewSite:GeeksQuiz.com"
m = len(X)
n = len(Y)

# Function call
print(LCSubStr(X, Y, m, n))

# This code is contributed by avanitrachhadiya2155
