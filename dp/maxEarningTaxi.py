from typing import List
from bisect import bisect_left

def maxTaxiEarningstd(n: int, rides: List[List[int]]) -> int:
    def dp(index):
        print(index)
        if index == n:
            return 0
        s, e, t = rides[index]
        #not pick the current number
        ans = dp(index + 1)
        #pick the current number, next aavailable slot
        #bisect_left is binary search
        j = bisect_left(rides,[e,0,0])
        print(j,e)
        ans = max(ans,e - s + t + dp(j))
        return ans

    n = len(rides)
    rides.sort()
    return dp(0)

def maxTaxiEarningsbu(n: int, rides: List[List[int]]) -> int:
    rides.sort()
    dp = [0] * (n + 1)
    print(dp)

    j = len(rides) - 1
    for i in range(n-1,-1,-1):
        #not pick any passenger at ith point
        dp[i] = dp[i+1]
        print(i,j,dp,rides[j])
        while j>=0 and rides[j][0] == i:
            s,e,t = rides[j]
            dp[i] = max(dp[i],e-s+t + dp[e])
            j -=1
    print(dp)
    #Because constraint mentioned is 1
    return dp[1]
if __name__ == '__main__':
    #print(maxTaxiEarningsbu(20,[[1,6,1],[3,10,2],[10,12,3],[11,12,2],[12,15,2],[13,18,1]]))
    print(maxTaxiEarningsbu(5,[[2,5,4],[1,5,1]]))