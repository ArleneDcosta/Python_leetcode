def numEnclaves(grid):
    def dfs(i, j):
        # Check boundaries and if the cell is land
        if i < 0 or j < 0 or i >= total_rows or j >= total_cols or grid[i][j] == 0:
            return 0
        # Mark cell as visited by setting it to 0
        grid[i][j] = 0

        # Perform DFS in all four directions and count this cell
        count = 1
        count += dfs(i - 1, j)
        count += dfs(i + 1, j)
        count += dfs(i, j - 1)
        count += dfs(i, j + 1)
        return count

    total_rows = len(grid)
    total_cols = len(grid[0])

    # Remove lands connected to borders by marking them
    for i in range(total_rows):
        for j in [0, total_cols - 1]:  # First and last column
            dfs(i, j)
    for j in range(total_cols):
        for i in [0, total_rows - 1]:  # First and last row
            dfs(i, j)

    # Count remaining enclaves
    result = 0
    for i in range(1, total_rows - 1):
        for j in range(1, total_cols - 1):
            if grid[i][j] == 1:
                result += dfs(i, j)

    return result

if __name__ == '__main__':
    # print(numEnclaves([[0,1,1,0],[0,0,1,0],[0,0,1,0],[0,0,0,0]]))
    print(numEnclaves([[0,0,0,0],[1,0,1,0],[0,1,1,0],[0,0,0,0]]))