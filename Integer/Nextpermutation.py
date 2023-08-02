def nextPermutation(nums):
    n = len(nums)
    index, next = -1, 0
    for i in reversed(range(1,n)):
        if nums[i-1] < nums[i]:
            index = i-1
            break
    print index   
    if index == -1:
        nums.reverse()
    else:
        for i in reversed(range(n)):
            if nums[i] > nums[index]:
                next = i
                break
        nums[index], nums[next] = nums[next], nums[index]
        reverse(nums,index+1)
    return nums
	#function to reverse the list from given index
def reverse(arr, start):
    end = len(arr)-1
    while start < end:
        arr[start], arr[end] = arr[end], arr[start]
        start += 1
        end -= 1


print nextPermutation([3,1,4,2])
