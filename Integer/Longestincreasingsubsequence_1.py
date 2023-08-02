def lengthOfLIS(nums):
    n=len(nums)
    stack=[]
    top=-1
    stack.append(nums[0])
    top+=1
    for i in range(1,n):
        if stack[top]<nums[i]:
            stack.append(nums[i])
            top+=1
        else:
            idx=binary(stack,top,nums[i])
            stack[idx]=nums[i]
    return top+1,stack
def binary(stack,top,curr):
    low=0
    high=top
    while low<high:
        mid=(low+high)>>1
        if stack[mid]<curr:
            low=mid+1
        else:
            high=mid
    return high
print lengthOfLIS([0,8,4,12,2,10,6,14,1,9,5,13,3,11,7,15])
