from typing import List
from bisect import bisect_left

def countSmaller(nums: List[int]) -> List[int]:
    '''arr, ans = sorted(nums), []          
    for num in nums:
        i = bisect_left(arr,num)  
        ans.append(i)                    
        del arr[i]                       
        
    return ans'''
    def sort(indexes):
        half = len(indexes) // 2
        if half:
            left, right = sort(indexes[:half]), sort(indexes[half:])
            print(left,right,indexes)
            for i in range(len(indexes) - 1, -1, -1):
                if not right or (left and nums[left[-1]] > nums[right[-1]]):
                    smaller[left[-1]] += len(right)
                    indexes[i] = left.pop()
                else:
                    indexes[i] = right.pop()
        return indexes

    smaller = [0] * len(nums)
    print(sort(list(range(len(nums)))))
    return smaller

if __name__ == '__main__':
    print(countSmaller(nums = [5,2,6,1]))
    # print(countSmaller(nums = [4,3,6,7]))
    # print(countSmaller(nums = [-1,-1]))
    # print(countSmaller(nums = [2,0,1]))