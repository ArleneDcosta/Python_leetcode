from collections import Counter, defaultdict
from typing import List
import math

def countKDifferencenew(nums: List[int], k: int) -> int:
    freq = defaultdict(int)
    count = 0
    
    for num in nums:
        print(num, num - k, num + k)
        count += freq[num - k] + freq[num + k]
        freq[num] += 1

    return count

def countKDifference(nums: List[int], k: int) -> int:
    ans = 0
    for i in range(0, len(nums)):
        for j in range(i+1, len(nums)):
            if abs(nums[i] - nums[j]) == k:
                ans += 1

    return ans

if __name__ == '__main__':
    nums = [1,2,2,1]
    k = 1
    print(countKDifferencenew(nums,k))


    nums = [3,2,1,5,4]
    k = 2
    print(countKDifferencenew(nums,k))

    nums = [1,1,1]
    k = 0
    print(countKDifferencenew(nums,k))