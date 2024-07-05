from typing import List
from collections import Counter,defaultdict
from heapq import heappop,heappush

def isPossibleheap(nums: List[int]) -> bool:
    end = defaultdict(list)
    for num in nums:
        if num - 1 not in end:
            heappush(end[num],1)
        else:

            pre_length = heappop(end[num-1])
            if len(end[num-1]) == 0:
                del end[num-1]
            heappush(end[num],pre_length+1)
        print(end)
    if any(min(end[num]) < 3 for num in end):
        return False
    return True

def isPossible(nums: List[int]) -> bool:
    counter = Counter(nums)
    end = defaultdict(int)
    # print(counter,end)

    for num in nums:
        if counter[num]:
            # suppose 1,2,3, and now u are at 4 [4 and 5 have aldready been taken care of] so that 4 cab be a part of [1,2,3,4]
            if end[num - 1]:
                end[num - 1]-= 1
                end[num] += 1
                counter[num] -= 1
            elif counter[num+1] and counter[num+2]:
                end[num+2] += 1
                counter[num + 1] -= 1
                counter[num + 2] -= 1
                counter[num] -= 1
            else:
                return False
        # print(num,counter,end)
    return True

if __name__ == '__main__':
    print(isPossible([1,2,3,3,4,5]))
    # print(isPossible([1,2,3,3,4,4,5,5]))
    # print(isPossible([1,2,3,4,4,5]))
    # print(isPossible([1,2,2,3,3,4,4,5]))