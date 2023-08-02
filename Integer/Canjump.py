def canJump(nums):
    last = len(nums)-1
    i=last-1
    while(i>=0):
        print(i,nums[i],last)
        if i+nums[i] >= last:
            last = i
        i-=1
    return last <=0
    
    
        
print(canJump([2,3,1,1,4]))
print(canJump([3,2,1,0,4]))
print(canJump([0,1]))
print(canJump([2,5,0,0]))
print(canJump([1,2]))
print(canJump([2,0,0]))
