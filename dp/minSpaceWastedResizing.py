import sys
from functools import lru_cache

# Greedy algorithms means choosing the best approach from a different approaches while DP deals with trying all and selecting best
# approaches from all of them

def min_space_wasted_resizing(nums,k):
    @lru_cache(None)
    def dp(i,k):
        if i == n:
            return 0
        if k == -1:
            #This will make ans very big so smaller value will be chosen and this value wont be chosen
            return sys.maxsize

        ans =  sys.maxsize
        newsize = 0
        rs = 0
        for j in range(i,n):
            newsize = max(newsize,nums[j])
            rs += nums[j]
            ans =  min(ans,newsize * (j-i + 1) - rs + dp(j+1,k-1))

        return ans

    n =  len(nums)
    return dp(0,k)

if __name__ == '__main__':
    print(min_space_wasted_resizing([10,20,15,30,20],2))