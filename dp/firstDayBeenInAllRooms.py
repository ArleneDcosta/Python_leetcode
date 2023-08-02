def firstDayBeenInAllRooms(nextVisit) -> int:
    n = len(nextVisit)
    dp = [0] * n

    for i in range(1,n):
        next = nextVisit[i-1]

        dp[i] = dp[i-1] + 2 + (dp[i-1] - dp[next])

    mod = 10**9 + 7
    return dp[-1] % mod


print(firstDayBeenInAllRooms([0,1,2,3,1,5]))