from typing import List
from functools import lru_cache

def solve(matrixSize:int,row:int, col:int) :
    matrix = [[1] * matrixSize for _ in range(0,matrixSize)]

    @lru_cache(None)
    def dfs(totalSum,currSum,r,c):

        if r >= len(matrix)-1 and c >=len(matrix)-1:
            if currSum + 1 < totalSum:
                totalSum = currSum + 1
            return totalSum

        currSum +=1

        if r < len(matrix) -1:
            totalSum = dfs(totalSum,currSum,r+1,c)

        if c < len(matrix) - 1:
            totalSum = dfs(totalSum, currSum, r, c+1)

        newSum = dfs(totalSum, currSum, r+1, c+1)
        totalSum = min(newSum,totalSum)
        return totalSum

    return(dfs(1000000,0,row,col))

# Cannot pass a list to a function when lru_cache is used as a generator
if __name__ == '__main__':
    print(solve(2,0,0))