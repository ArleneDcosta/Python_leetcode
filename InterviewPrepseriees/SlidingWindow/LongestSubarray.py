from typing import List


def longestSubarray(nums: List[int], limit: int) -> int:
    def helper(mid):
        current_count = 0
        minval = min(nums[i:i+mid])
        maxval = min(nums[i:i+mid])
        for i in range(mid, len(nums)):
            if nums[i] > maxval:
                maxval = nums[i]
            if nums[i] < minval:
                minval  = nums[i]
            if maxval - minval <= limit:
                current_count += 1

        return current_count

    left = 1
    right = len(nums)
    while(left < right):
        mid = left + (right - left + 1) // 2
        if helper(mid):
            left = mid
        else:
            right = mid - 1


    return left


def longestSubarrayOp(nums,limit):
    i, maxq, minq = 0, [], []
        
    for num in nums:
        while len(maxq) and num > maxq[-1]: maxq.pop()
        while len(minq) and num < minq[-1]: minq.pop()
            
        maxq.append(num)
        minq.append(num)
        
        if maxq[0] - minq[0] > limit:
            if maxq[0] == nums[i]: maxq.pop(0)
            if minq[0] == nums[i]: minq.pop(0)
            i += 1
            
    return len(nums) - i

if __name__ == "__main__":
    nums = [10,1,2,4,7,2]
    limit = 5
    # print(longestSubarrayOp(nums,limit))

    nums = [8,2,4,7]
    limit = 4
    print(longestSubarrayOp(nums,limit))

    nums = [100, 2, 3, 4, 5, 100, 1]
    limit = 4
    print(longestSubarrayOp(nums,limit))