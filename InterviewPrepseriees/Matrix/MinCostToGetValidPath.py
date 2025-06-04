from typing import List

def minCostincorrect(grid: List[List[int]]) -> int:
    dir = {1 : [0,1], 2: [0,-1], 3: [1,0], 4: [-1,0]}

    def dfs(cost,i,j):
        print(i,j)
        if i == len(grid) - 1 and j == len(grid[0]) - 1:
            return cost
        if i >= len(grid) or j < 0 or j >= len(grid[0]): 
            cost += 1
            return cost
    
        if grid[i][j] == 1:
            cost += dfs(cost, i + dir[1][0],j + dir[1][1])
        if grid[i][j] == 2:
            cost += dfs(cost, i + dir[2][0],j + dir[2][1])
        if grid[i][j] == 3:
            cost += dfs(cost, i + dir[3][0],j + dir[3][1])
        
        if grid[i][j] == 4:
            cost += dfs(cost, i + dir[4][0],j + dir[4][1])

        return cost

    return dfs(0,0,0)

def minCost(grid: List[List[int]]) -> int:
        num_rows, num_cols = len(grid), len(grid[0])

        # Initialize all cells with max value
        min_changes = [[float("inf")] * num_cols for _ in range(num_rows)]
        min_changes[0][0] = 0

        while True:
            # Store previous state to check for convergence
            prev_state = [row[:] for row in min_changes]

            # Forward pass: check cells coming from left and top
            for row in range(num_rows):
                for col in range(num_cols):
                    # Check cell above
                    if row > 0:
                        min_changes[row][col] = min(
                            min_changes[row][col],
                            min_changes[row - 1][col]
                            + (0 if grid[row - 1][col] == 3 else 1),
                        )
                    # Check cell to the left
                    if col > 0:
                        min_changes[row][col] = min(
                            min_changes[row][col],
                            min_changes[row][col - 1]
                            + (0 if grid[row][col - 1] == 1 else 1),
                        )

            # Backward pass: check cells coming from right and bottom
            for row in range(num_rows - 1, -1, -1):
                for col in range(num_cols - 1, -1, -1):
                    # Check cell below
                    if row < num_rows - 1:
                        min_changes[row][col] = min(
                            min_changes[row][col],
                            min_changes[row + 1][col]
                            + (0 if grid[row + 1][col] == 4 else 1),
                        )
                    # Check cell to the right
                    if col < num_cols - 1:
                        min_changes[row][col] = min(
                            min_changes[row][col],
                            min_changes[row][col + 1]
                            + (0 if grid[row][col + 1] == 2 else 1),
                        )
            # If no changes were made in this iteration, we've found optimal solution
            if min_changes == prev_state:
                break
        print(min_changes)
        return min_changes
if __name__ == '__main__':
    grid = [[1,1,1,1],[2,2,2,2],[1,1,1,1],[2,2,2,2]]
    print(minCost(grid)[len(grid)-1][len(grid[0])-1])


