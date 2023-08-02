def numOfSubarrayBoundedMax(nums,left,right):
    ans =  cnt  = 0
    prev = -1
    for i,c in enumerate(nums):
        if left <= nums[i] <= right:
            cnt = i - prev
        elif nums[i] > right:
            prev = i
            cnt = 0
        # implicit handling of case when nums[i] < left value will contain the same count as prev but will not include itself
        ans += cnt
    return ans
#Example: 2,3,2,3
#here at 0 it is 1 , then it is 2 where 3 itself and [2,3] so it goes on



print(numOfSubarrayBoundedMax([2,3,1,4,5],2,3))