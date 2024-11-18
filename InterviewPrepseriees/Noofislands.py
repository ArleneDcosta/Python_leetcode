def numIslands(grid):
    row = len(grid)
    col = len(grid[0])
    def dfs(i,j):
        if i < 0 or j < 0 or i >= row or j >= col or grid[i][j] == '0':
            return
        grid[i][j] = '0'
        dfs(i-1,j)
        dfs(i+1,j)
        dfs(i,j-1)
        dfs(i,j+1)

        return
    res = 0
    for i in range(row):
        for j in range(col):
            if grid[i][j] == '1':
                res += 1
                dfs(i, j)

    return res

if __name__ == '__main__':
    grid = [
        ["1", "1", "1", "1", "0"],
        ["1", "1", "0", "1", "0"],
        ["1", "1", "0", "0", "0"],
        ["0", "0", "0", "0", "0"]
    ]
    print(numIslands(grid))
    grid = [
        ["1", "1", "0", "0", "0"],
        ["1", "1", "0", "0", "0"],
        ["0", "0", "1", "0", "0"],
        ["0", "0", "0", "1", "1"]
    ]
    print(numIslands(grid))