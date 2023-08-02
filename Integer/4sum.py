def solve(nums,target):
    res=[]
    nums.sort()

    for i,a in enumerate(nums):
        if i > 0 and a == nums[i-1]:
            continue

        l,r = i+1, len(nums)-1
        while l < r:
            li = l+1
            ri = r
            while li < ri:
                fourSum = a + nums[l] + nums[li] + nums[ri]
                if fourSum > target:
                    ri-=1
                elif fourSum < target:
                    li+=1
                else:
                    if [a,nums[l],nums[li],nums[ri]] not in res:
                        res.append([a,nums[l],nums[li],nums[ri]])
                    li+=1 
                    while(nums[li] == nums[li-1] and li< ri):
                        li += 1
            l +=1
    return res
print solve([1,0,-1,0,-2,2],0)
print solve([2,2,2,2,2],8)
