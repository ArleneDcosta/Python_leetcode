from functools import lru_cache
def maxAlternatingSum(nums):
    @lru_cache(None)
    def dp(i , parity):
        if i == n:
            return 0

        #not pick the current number
        ans = dp(i+1,parity)

        #pick current number
        if parity == 0:
            ans = max(ans, dp(i+1, parity ^ 1) + nums[i])
        else:
            ans = max(ans, dp(i + 1, parity ^ 1) - nums[i])
        return ans

    n = len(nums)
    return dp(0,0)

print(maxAlternatingSum([5,6,7,8]))
print(maxAlternatingSum([4,2,5,3]))
