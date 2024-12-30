from typing import List

def climbstairs(n):
    dp = [0] * (n + 1)

    dp[0] = 1
    dp[1] = 1
    for i in range(2,n+1):
        dp[i] = dp[i-1] + dp[i-2]

    return(dp[n])



if __name__ == '__main__':
    print(climbstairs(3))
    print(climbstairs(4))
    print(climbstairs(5))
