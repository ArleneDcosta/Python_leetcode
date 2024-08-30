from typing import List


def minMoves(nums: List[int], limit: int) -> int:
    cval = []
    n = len(nums)
    for i in range(0,len(nums)):
        cval.append([nums[i],nums[n-1-i]])
    print(cval)




if __name__ == '__main__':
    print(minMoves([1,2,4,3],4))