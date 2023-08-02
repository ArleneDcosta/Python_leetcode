from typing import List

def arrayNesting(nums: List[int]) -> int:
    n = len(nums)
    ans = 0
    seen = [False] * n
    for num in nums:
        l = 0
        while not seen[num]:
            l += 1
            seen[num] = True
            num = nums[num]
        ans = max(ans, l)

    return ans

if __name__ == '__main__':
    print(arrayNesting([0,2,3,4,1]))