def removeDuplicates(nums):
    d = {}
    for number in nums:
        if number in d:
            d[number]+=1
        else:
            d[number]=1
                
    print(d.keys())
    return len(d.keys())
    '''     left = 0
        right = 0
        while right < len(nums) - 1:
            right += 1
            while right < len(nums) and nums[left] == nums[right]:
                nums.pop(right)
            left += 1
        print(nums)
        return len(nums)'''
print(removeDuplicates([1,1,2]))
