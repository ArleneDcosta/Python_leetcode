from typing import List

def minimumOperations(nums: List[int]) -> int:
    no_of_operations = 0
    while len(set(nums)) != len(nums):
        nums = nums[3:]
        no_of_operations += 1
    
    return no_of_operations

def minimumOperationsOp(nums: List[int]) -> int:
    seen = [False] * 128
    for i in range(len(nums) - 1, -1, -1):
        if seen[nums[i]]:
            return i // 3 + 1
        seen[nums[i]] = True
    return 0


if __name__ == '__main__':
    nums = [3,7,12,12,3,14,1,1]
    print(minimumOperations(nums))

    