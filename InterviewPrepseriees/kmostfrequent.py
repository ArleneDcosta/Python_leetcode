from typing import List
from collections import Counter
import heapq
from collections import defaultdict

def topKFrequentold(nums: List[int], k: int) -> List[int]:
        if k == 0:
            return []
        count = defaultdict(int)
        for no in nums:
            count[no] += 1

        countlist = []
        for key in count:
            countlist.append((key,count[key]))

        countlist = sorted(countlist,key= lambda x:x[1], reverse=True)

        res = []
        for i in range(0,k):
            res.append(countlist[i][0])

        print(countlist)
        return res


def topKFrequent(nums: List[int], k: int) -> List[int]:
    cnts = Counter(nums)
    heap = []

    for n, cnt in cnts.items():
        heapq.heappush(heap, (cnt, n))
        if len(heap) > k:
            heapq.heappop(heap)

    return [n for cnt, n in heap]
