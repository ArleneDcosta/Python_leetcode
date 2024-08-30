from typing import List
import sys

def mincostTicketstd(days: List[int], costs: List[int]) -> int:
    print(days)
    def dp(i):
        print(i)
        if i in memo:
            return memo[i]
        if i > days[-1] or i <= 0:
            return 0
        ans = sys.maxsize
        if i not in days_set:
            ans = dp(i - 1)
        else:
            ans = min(dp(i - 1) + costs[0],dp(i - 7) + costs[1],dp(i - 30) + costs[2] )
        memo[i] = ans
        return ans

    memo = {}
    days_set = set(days)

    return dp(days[-1])

def mincostTicketsbu(days: List[int], costs: List[int]) -> int:
    dp = [sys.maxsize] * (days[-1] + 1)
    dp[0] = 0
    days_set = set(days)
    for i in range(1,(days[-1] + 1)):
        if i not in days_set:
            dp[i] = dp[i-1]
        else:
            dp[i] = min(dp[i-1] + costs[0],dp[max(0,i-7)] + costs[1],dp[max(0,i-30)] + costs[2])

    return dp[days[-1] ]

#https://leetcode.com/problems/minimum-cost-for-tickets/description/
if __name__ == '__main__':
    print(mincostTicketstd([1,4,6,7,8,20],[2,7,15]))
    #days = [1,2,3,4,5,6,7,8,9,10,30,31], costs = [2,7,15]