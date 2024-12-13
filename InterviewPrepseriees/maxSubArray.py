

def maxSubArray(nums):
    maxResult = -100000
    currSum = 0
    for ele in nums:
        currSum += ele
        maxResult = max(maxResult, currSum)
        if currSum < 0:
            currSum = 0
    return maxResult


def maxSubArraydc(self, nums):
    def helper(nums, left, right):
        # Base case: only one element
        if left == right:
            return nums[left]

        # Find the middle of the current subarray
        mid = (left + right) // 2

        # Find max subarray sum in left half
        left_max = helper(nums, left, mid)
        # Find max subarray sum in right half
        right_max = helper(nums, mid + 1, right)
        # Find max subarray sum crossing the middle
        cross_max = maxCrossingSum(nums, left, mid, right)

        # Return the maximum of the three
        return max(left_max, right_max, cross_max)

    def maxCrossingSum(nums, left, mid, right):
        # Include elements on the left of mid
        left_sum = float('-inf')
        curr_sum = 0
        for i in range(mid, left - 1, -1):
            curr_sum += nums[i]
            left_sum = max(left_sum, curr_sum)

        # Include elements on the right of mid
        right_sum = float('-inf')
        curr_sum = 0
        for i in range(mid + 1, right + 1):
            curr_sum += nums[i]
            right_sum = max(right_sum, curr_sum)

        # Combine sums from both sides of mid
        return left_sum + right_sum

    return helper(nums, 0, len(nums) - 1)


if __name__ == '__main__':
    print(maxSubArray([-2,1,-3,4,-1,2,1,-5,4]))