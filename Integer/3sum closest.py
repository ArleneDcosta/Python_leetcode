def solve(nums,target):
    res=1000000
    nums.sort()

    for i,a in enumerate(nums):
        if i > 0 and a == nums[i-1]:
            continue

        l,r = i+1, len(nums)-1
        while l < r:
            threeSum = a + nums[l] + nums[r]
            if abs(target - threeSum)  <  abs(target - res):
                res = threeSum
            if threeSum > target :
                r-=1
                
            elif threeSum < target:
                l+=1
                
            else:
                return threeSum
                
    return res
print solve([-1,2,1,-4],1)
print solve([0,0,0],1)
print solve([1,1,1,0],-100)
