def climbStairs(n): 
    dp = [0]*n
    return climb(n, dp)

def climb(n,dp):
    if(n<0):
        return 0
        
    if(n==0):
        return 1

    if(dp[n-1] != 0):
        return dp[n-1]
    dp[n-1] = climb(n-1, dp) + climb(n-2, dp)
    return dp[n-1]


print(climbStairs(3))
dp[3] = dp[2] + dp[1]

dp[2] = dp[1] + dp[0]
dp[1] = dp[0] + dp[-1]
      = 1 + 0 = 1
dp[1] = 1
dp[2] = 2
dp[3] = 3
