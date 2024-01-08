import sys
from typing import List
from functools import lru_cache
'''
dp for maintaining of states whether that particular state is completed.
dp(i,bitmask) = i = current node and the subsequent node bitmask
When i reaches the end, everything from first group is over
Check nything from second group has bitmask equal to 0
'''
def connectTwoGroups(cost: List[List[int]]) -> int:
    @lru_cache(None)
    def dp(i,mask) -> int:
        if i == size1:
            ans2 = 0
            for j in range(size2):
                if mask & (1 << j) == 0:
                    ans2 += min_cost2[j]

            return ans2
        ans = sys.maxsize

        for j in range(size2):
            ans = min(ans,dp(i+1, mask | (1 << j)) + cost[i][j])
        return ans

    #memo = {}[ lru_cache handles it for us
    size1 = len(cost) # first group
    size2 = len(cost[0]) # length of second group
    min_cost2 = [sys.maxsize] * size2
    # For all group 2 elements min conn to group 1 elements
    for j in range(size2):
        for i in range(size1):
            min_cost2[j] = min(min_cost2[j],cost[i][j])
    print(min_cost2)
    return dp(0,0)

if __name__ == '__main__':
    # Below example 2 in the if size1 loop and 1 in the below forloop and last one in the if size1 block
    print(connectTwoGroups(cost = [[1, 3, 5], [4, 1, 1], [1, 5, 3]]))

'''[1,3,5] Connected from A to 1 2 and 3[4 1 1]  connected from B to 1 2 and 3 and '''