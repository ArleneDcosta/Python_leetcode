def largestMagicSquare(grid):
    m = len(grid)
    n = len(grid[0])

    rowPreSum = []
    for i in range(m):
        presum = {-1: 0}
        for j in range(n):
            presum[j] = presum[j-1] + grid[i][j]

        rowPreSum.append(presum)

    print(rowPreSum)

    colPreSum = []
    for j in range(n):
        presum = {-1: 0}
        for i in range(m):
            presum[i] = presum[i-1] + grid[i][j]
        colPreSum.append(presum)

    print(colPreSum)
    ans  = 1
    for i in range(m):
        for j in range(n):
            for length in range(2,min(m-i,n-j)+1):
                ssum = rowPreSum[i][j+length - 1] - rowPreSum[i][j-1]
                diagonal = antiDiagonal = 0
                flag = True
                for l in range(length):
                    row = rowPreSum[i + l][j + length -1] - rowPreSum[i+l][j -1]
                    if row!= ssum:
                        flag = False
                        break
                    col = colPreSum[j + l][i + length - 1] - colPreSum[j + l][i - 1]
                    if col != ssum:
                        flag = False
                        break
                    diagonal += grid[i+l][j+l]
                    antiDiagonal += grid[i+l][j+(length - l - 1)]
                if flag and diagonal == antiDiagonal == ssum:
                    ans = max(ans,length)

    return ans
print(largestMagicSquare([[7,1,4,5,6],[2,5,1,6,4],[1,5,4,3,2],[1,2,7,3,4]]))
