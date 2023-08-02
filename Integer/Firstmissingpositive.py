def firstMissingPositive(nums):
    '''input = set(nums)
    count=1
    while(1):
        if count not in input:
            return count
        count += 1'''
    nums.sort()
    for i in range(0,len(nums)):
        if i+1 not in nums:
            return i+1
    return nums[len(nums)-1]+1
    #return count
print firstMissingPositive([1,2,0])
