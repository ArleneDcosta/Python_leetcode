
# Odds of being at zero is 1 because always will start from 0
# Odds of being at one is 1/maxpoints (assume 10) = 0.1
# Odds of being 2 aftre 0 is 1 * 0.1 = 0.1 and odds of being another 1 after 1 is 0.1 * 0.1 =  0.01 + 0.1 = 0.11

def new21Game(n: int, k: int, maxPts: int) -> float:
    if k == 0 or n >= k + maxPts:
        return 1.0  # Special case: always wins

    dp = [0.0] * (n + 1)
    dp[0] = 1.0
    windowSum = 1.0
    result = 0.0

    for x in range(1, n + 1):
        dp[x] = windowSum / maxPts
        print(dp)
        if x < k:
            windowSum += dp[x]
        # So in less than k assume k = 2 so at 0 u can choose draw anything 1 to 10 if u get 1 u can drow again but if 2 u stop
        # So assume u have 3 you can add the prev because its 1 and then u can get 3 so 
        elif k <= x <= min(n, k + maxPts - 1): # To avoid cases when n > k + maxpts
            print(windowSum,maxPts,dp[x])
            result += dp[x]  # She stops drawing at x >= k

        if x - maxPts >= 0:
            windowSum -= dp[x - maxPts]

    return result


if __name__ == '__main__':
    n = 10
    k = 1
    maxPts = 10
    print(new21Game(n,k,maxPts))


    # n = 21
    # k = 17
    # maxPts = 10
    # print(new21Game(n,k,maxPts))