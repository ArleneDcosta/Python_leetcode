
def rob(nums):
    dp = [nums[i] for i in range(len(nums))]
    for i in range(0,len(nums)):
        for j in range(i+2,len(nums)):
            dp[j] = max(dp[j],dp[i] + nums[j])

    return max(dp[-1],dp[-2])

def rob_optimized(nums):
    if len(nums) == 0:
        return 0
    memo = [0] * (len(nums) + 1)
    memo[0] = 0
    memo[1] = nums[0]
    for i in range(1, len(nums)):
        val = nums[i]
        memo[i + 1] = max(memo[i], memo[i - 1] + val)
    return memo[len(nums)]

if __name__ == '__main__':
    print(rob([2,7,9,3,1]))
    print(rob([2,1,1,2]))