from typing import List

def wiggleMaxLength(nums: List[int]) -> int:
    if len(nums) == 1:
        return 1
    res = []
    currpos = 1
    currneg = 0

    j = 0

    while(True and len(nums) > 2 and j < len(nums)-1):
        if nums[j] < nums[j+1]:
            res.append(nums[j])
            currpos,currneg = 0, 1
            break

        if nums[j] > nums[j+1]:
            res.append(nums[j])
            currpos,currneg = 1, 0
            break
        j += 1

    for i in range(j+1,len(nums)-1):
        if currpos == 1:
            if nums[i] < nums[i+1]:
                res.append(nums[i])
                currpos,currneg = 0,1
        elif currneg == 1:
            if nums[i] > nums[i+1]:
                res.append(nums[i])
                currpos,currneg = 1,0

    if currpos == 1:
        if res and nums[-1] < res[-1]:
            res.append(nums[-1])
    
    if currneg == 1:
        if res and nums[-1] > res[-1]:
            res.append(nums[-1])

    if len(res) == 0:
        return 1
    return len(res)

if __name__ == '__main__':
    nums = [1,7,4,9,2,5]
    print(wiggleMaxLength(nums))

    nums = [1,17,5,10,13,15,10,5,16,8]
    print(wiggleMaxLength(nums))

    nums = [1,2,3,4,5,6,7,8,9]
    print(wiggleMaxLength(nums))

    nums = [3,3,3,2,5]
    print(wiggleMaxLength(nums))

    nums = [0,0,0]
    print(wiggleMaxLength(nums))