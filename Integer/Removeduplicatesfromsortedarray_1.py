MAX_DUPLICATES = 2
def removeDuplicates(nums):
    i = 0

    for num in nums:
        if i < self.MAX_DUPLICATES or nums[i - self.MAX_DUPLICATES] != num:
            nums[i] = num
            i += 1

    return i,nums


print(removeDuplicates([]))
