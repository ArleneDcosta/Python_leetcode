from typing import List
def minKBitFlips(nums: List[int], k: int) -> int:
    n = len(nums)
    ans = 0
    hasEverFlipped = [0] * n
    validCountCurrentIdx = 0
    for i in range(n):
        if i >= k:
            if hasEverFlipped[i-k]:
                validCountCurrentIdx -= 1
        # If flipped before: 0 and 0 means not flipped and 1  1 means 1 got converted to 0 and flipped before
        # So below logic will flip
        if validCountCurrentIdx % 2 == nums[i]:
            if i + k > n:
                return -1
            validCountCurrentIdx += 1
            hasEverFlipped[i] = 1
            ans +=1
    return ans

def minKBitFlipsbf(nums: List[int], k: int) -> int:
    n = len(nums)
    ans = 0

    for i in range(n):
        if nums[i] == 0:
            if i + k > n:
                return -1
            nums[i:i+k] = [num ^ 1 for num in nums[i:i+k]]
            ans += 1
        print(nums,ans)


if __name__ == '__main__':
    # print(minKBitFlips([0,0,0,1,0,1,1,0],3))
    # print(minKBitFlips([1,1,0],2))
    print(minKBitFlips([0,1,0,1],4))