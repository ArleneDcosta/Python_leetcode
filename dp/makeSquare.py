from functools import lru_cache
def makeSquare(matchsticks) -> bool:
    @lru_cache(None)
    def dp(mask,sidesRemain,currSideRemain):
        #If all sides are used and done and mask means every value is used
        if sidesRemain == 0 and mask == 0:
            return True

        for i in range(len(matchsticks)):
            #Since mask is initialised as 1
            if mask & (1<<i) != 0:
                if matchsticks[i] <= currSideRemain:
                    newRemain  = currSideRemain - matchsticks[i]
                    if dp( mask ^ (1 << i),sidesRemain if newRemain else sidesRemain - 1, target if not newRemain else newRemain):
                        return True
        return False
    total = sum(matchsticks)
    if total % 4:
        return False
    target = total // 4
    n = len(matchsticks)
    return dp((1<<n)-1,4,target)


print(makeSquare([1,1,2,2,2]))
#Here constraint for array was set as 15 hence bit is allocated for every index