
#Time limit exceeded as used recursion
def calculatepath(row,col,m,n,sum,result,dp):
    if row == m-1 and col == n-1:
        print(row,col)
        sum += dp[row][col]
        result.append(sum)
        return (result)
    if(row < m and col < n):
        sum += dp[row][col]
        print(row,col)
        if row < m:
            result = calculatepath(row+1,col,m,n,sum,result,dp)
        if col < n:
            result = calculatepath(row,col+1,m,n,sum,result,dp)
    return result
    
        
def minpathsum(dp):
    #dp=[[0 for i in range(n)] for j in range(m)]
    m = len(dp)
    n = len(dp[0])
    print(calculatepath(0,0,m,n,0,[],dp))
#
def minPathSum(grid):
    col=len(grid[0])
    row=len(grid)
    dp=[[0 for i in range(col)] for j in range(row)]
    dp[row-1][col-1]=grid[row-1][col-1]
    ###initialize the last col:
        
    for r in range(row-2,-1,-1):
        dp[r][col-1]=dp[r+1][col-1]+grid[r][col-1]
    ###initialize the last row
    for c in range(col-2,-1,-1):
        dp[row-1][c]=dp[row-1][c+1]+grid[row-1][c]
    for c in range(col-2,-1,-1):
        for r in range(row-2,-1,-1):
            dp[r][c]=min(dp[r+1][c]+grid[r][c],dp[r][c+1]+grid[r][c])
    return dp[0][0]
print(minpathsum([[1,3,1],[1,5,1],[4,2,1]]))


