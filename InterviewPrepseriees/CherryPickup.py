from typing import List
import sys

def cherryPickup(grid: List[List[int]]) -> int:
    def dp(r1,c1,r2,c2):
        if (r1,c1,r2,c2) in memo:
            return memo[(r1,c1,r2,c2)]
        
        if r1 > n-1 or c1 > n-1 or r2 > n-1 or c2 > n-1 or grid[r1][c1] == -1 or grid[r2][c2] == -1:
            return -sys.maxsize
        
        if r1 == c1 == n - 1:
            return grid[r1][c1]

        cur_cherry = 0
        if r1 == r2 and c1 == c2:
            cur_cherry = grid[r1][c1]
        else:
            cur_cherry = grid[r1][c1] + grid[r2][c2]

        next_cherry = -sys.maxsize

        directions = [(1,0),(0,1)]
        for d1 in directions:
            for d2 in directions:
                nr1 = r1 + d1[0]
                nc1 = c1 + d1[1]
                nr2 = r2 + d2[0]
                nc2 = c2 + d2[1]
                next_cherry = max(next_cherry,dp(nr1,nc1,nr2,nc2))

        cur_cherry += next_cherry
        memo[(r1,c1,r2,c2)] = cur_cherry
        return cur_cherry
    
    memo = {}
    n = len(grid)
    ans = dp(0,0,0,0)

    return max(ans,0)

if __name__ == '__main__':
    print(cherryPickup([[0,1,-1],[1,0,-1],[1,1,1]]))