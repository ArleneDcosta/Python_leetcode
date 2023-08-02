def removeElement(nums, val):
    #nums = filter(lambda a: a != val, nums)
    numsdup = filter(lambda a: a != val, nums)
    print numsdup
    i=0
    for ele in numsdup:
        nums[i]=ele
        i+=1
    print(nums)
    return len(numsdup)
    '''if len(nums) == 0:
        return 0
    i = len(nums)-1
    while i>=0:
        if nums[i] is val:
            nums.pop(i)
            i=len(nums)
        i-=1
    return (len(nums))'''
print removeElement([0,1,2,2,3,0,4,1],2)
