from typing import List
from heapq import heapify,heappop,heappush

def findKthLargest(nums: List[int], k: int) -> int:
    maxele = max(nums)
    countdict = {}
    for no in nums:
        if no in countdict:
            countdict[no] += 1
        else:
            countdict[no] = 1

    for i in range(maxele, -10000, -1):
        if i in nums:
            if k == 1:
                return i
            else:
                k -= countdict[i]
                if k <= 0:
                    return i
    return min(nums)

def findKthLargesth(nums: List[int], k: int) -> int:
    heap = nums[:k]
    heapify(heap)

    for num in nums[k:]:
        if num > heap[0]:
            heappop(heap)
            heappush(heap, num)

    return heap[0]


if __name__ == '__main__':
    print(findKthLargest([3,2,1,5,6,4], k = 2))
    print(findKthLargest([3,2,3,1,2,4,5,5,6], k = 4))
    print(findKthLargest([3,3,3,3,3,3,3,3,3],k=8))