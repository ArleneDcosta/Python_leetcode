def dominantIndex(nums):
    maxele = max(nums)
    for i in range(0,len(nums)):
        if nums[i]==maxele:
            ans = i
        elif maxele < 2*(nums[i]):
            return -1
    return ans

dominantIndex([3, 6, 1, 0])

l = [1,2,3,4,5,6]
print l[:-2]
print l[::-2]
