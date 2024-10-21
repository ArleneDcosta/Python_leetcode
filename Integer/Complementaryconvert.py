import sys
from typing import List
from collections import defaultdict

#https://leetcode.com/problems/minimum-moves-to-make-array-complementary/

def minMoves(nums: List[int], limit: int) -> int:
    # diff is the no for efforts needed to make the array complimentary
    ssum = defaultdict(int)
    diff = defaultdict(int)

    n = len(nums)

    for i in range(n//2):
        a = nums[i]
        b = nums[n - i - 1]
        print(a,b)
        mmin = min(a,b)
        mmax = max(a,b)
        left = mmin + 1  # replace mmax element with smallest value < limit i.e 1
        right = mmax + limit  # Replace mmin element with max val (limit)

        diff[left] -= 1
        diff[right + 1] += 1
        ssum [a + b] += 1

    ans = sys.maxsize
    cur = n
    print(diff, ssum)
    # Below is for overlap so when entering reduce and exit + 1+

    for s in range(2,max(ssum)+1):
        #reducing the no of moves to make complementary
        print(cur,s,diff[s])
        cur += diff[s]

        ans = min(ans, cur - ssum[s])

    return ans


if __name__ == '__main__':
    print(minMoves([1,2,4,3],4))
    #print(minMoves([1, 2, 4, 1], 4))

#LOGIC
'''
consider 3,5 and limit 6
diff[start] -1 because that removes the effort make one element of the array to make (x,y) complemenatary like 
initially there are 4 elements [1,2,4,3] where (1,3) and (2,4) is pair
so when (1,3) where min (1,1) = 2
so only 1 among 2 will have to be changed  (since min is 2 and max is 3 + 4 since limit is 4 = 7 so if we get 8
then for (1,3) we have (4, 4 ) = 8 so both elements needed to be changed, else one element is needed
1 + 3 or

so in a pair with a higher, lower -> we reduce the higher to a smallest element ans its sum is lb
and if we keep the highest number then higher + (lower + limit) = hb
since higher cannot be greater than limit
'''