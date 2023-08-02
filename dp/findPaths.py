from functools import lru_cache
def findPaths(m,n,maxMove,startRow,startColumn):
    @lru_cache(None)
    def dp(i,j,moves):
        #if out of bounds return the correct value
        if i < 0 or j < 0 or i >= m or j >= n:
            return 1
        #if moves got exhausted before reaching value return 0
        if moves == 0:
            return 0

        ans = 0
        for d in directions:
            ni = i + d[0]
            nj = j + d[1]
            ans += dp(ni,nj,moves - 1)

        return ans

    directions = [(1,0),(-1,0),(0,1),(0,-1)]
    mod = 10**9 + 7
    return dp(startRow,startColumn,maxMove) % mod


print(findPaths(1,3,3,0,1))