def triangleNumber(nums): 
    count = 0
    nums.sort()
    for i in range(0,len(nums)-2):
        k = i + 2
        j = i + 1
        while(j < nums.length - 1 and nums[i] != 0):
            while (k < nums.length and nums[i] + nums[j] > nums[k]):
                k+=1
                count += k - j - 1
        return count
    

print triangleNumber([2,2,4,3])
