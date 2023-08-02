#make sure that sliding window has 0's less than or equal to k

def maxConsecutiveOnes(nums,k):
    def helper(length):
        flips = 0 #number of 0'z
        #first sliding window
        for i in range(length):
            flips += 1 ^ nums[i]
        if flips <= k:
            return True

        #next sliding window
        for i in range(length,n):
            flips += 1 ^ nums[i]
            flips -= 1 ^ nums[i-length]

            if flips <= k:
                return True

        return False

    n = len(nums)
    l = 0
    r = n
    while l < r:
        mid = l + (r - l + 1) // 2
        if helper(mid):
            l = mid
        else:
            r = mid - 1
        print(mid)
    return l


print(maxConsecutiveOnes([1,1,1,0,0,0,1,1,1,1,0],2))