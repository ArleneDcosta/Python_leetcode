#make sure that sliding window has 0's less than or equal to k

def maxConsecutiveOnes(nums,k):
    n = len(nums)
    l = 0
    ans = 0
    flips = 0

    for r in range(n):
        flips += 1 ^ nums[r]
        if flips > k:
            flips -= 1 ^ nums[l]
            l += 1
        if flips <= k:
            ans = max(ans, r-l + 1)
    return ans


print(maxConsecutiveOnes([1,1,1,0,0,0,1,1,1,1,0],2))