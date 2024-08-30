import heapq
import sys
from typing import List
from heapq import heappop , heappush

def minimumDeviation(nums: List[int]) -> int:
    pq = []
    mmin = sys.maxsize

    for num in nums:
        if num % 2 == 0:
            heapq.heappush(pq,-num )
            mmin = min(mmin, num )
        else:
            heapq.heappush(pq,-num * 2)
            mmin = min(mmin , num * 2)

    #even divide by 2, odd multiply by 2

    ans = sys.maxsize
    print(pq)
    while pq:
        print(pq)
        curr = -heapq.heappop(pq)
        print(f"Curr {curr}, Curr - mmin {curr - mmin}")
        print(f"Below {pq}")
        ans = min(ans, curr - mmin)

        if curr % 2:
            print(curr)
            break

        heapq.heappush(pq,- curr // 2)
        mmin = min(mmin, curr // 2)

    return ans

if __name__ == '__main__':
    # print(minimumDeviation(nums = [4,1,5,20,3]))
    print(minimumDeviation(nums=[7,1]))
    # print(minimumDeviation(nums = [1,2,3,4]))