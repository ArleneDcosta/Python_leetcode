
import sys
from collections import deque
from functools import lru_cache

def min_step_by_knight_dfs(matrixlen, knightPos, targetPos):
    knight_moves = [(-1, -2), (-2, -1), (-1, 2), (-2, 1), 
                    (1, -2), (2, -1), (1, 2), (2, 1)]
    
    memo = {}

    def dfs(i, j, visited):
        if (i, j) == targetPos:
            return 0
        if i < 0 or j < 0 or i >= matrixlen or j >= matrixlen:
            return sys.maxsize
        if (i, j) in visited:
            return sys.maxsize
        if (i, j) in memo:
            return memo[(i, j)]

        visited.add((i, j))  # mark as visited in current path
        min_steps = sys.maxsize
        for dx, dy in knight_moves:
            steps = dfs(i + dx, j + dy, visited)
            if steps != sys.maxsize:
                min_steps = min(min_steps, steps + 1)
        visited.remove((i, j))  # backtrack

        if min_steps != sys.maxsize:
            memo[(i, j)] = min_steps

        return min_steps

    result = dfs(knightPos[0], knightPos[1], set())
    return result if result != sys.maxsize else -1


from collections import deque

def min_step_by_knight_bfs(matrixlen, knightPos, targetPos):
    knight_moves = [(-1, -2), (-2, -1), (-1, 2), (-2, 1), (1, -2), (2, -1), (1, 2), (2, 1)]
    visited = [[False] * matrixlen for _ in range(matrixlen)]

    queue = deque()
    queue.append((knightPos[0], knightPos[1], 0)) 
    visited[knightPos[0]][knightPos[1]] = True

    while queue:
        x, y, steps = queue.popleft()
        if (x, y) == (targetPos[0], targetPos[1]):
            return steps
        for dx, dy in knight_moves:
            nx, ny = x + dx, y + dy
            if 0 <= nx < matrixlen and 0 <= ny < matrixlen and not visited[nx][ny]:
                visited[nx][ny] = True
                queue.append((nx, ny, steps + 1))
    
    return -1  # If unreachable


if __name__ == '__main__':
    print(min_step_by_knight_dfs(6,[2,1],[0,0]))