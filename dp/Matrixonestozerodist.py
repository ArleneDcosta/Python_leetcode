from collections import deque
import sys

def update_matrix(mat):
    m = len(mat)
    n = len(mat[0])
    ans = [[sys.maxsize] * n for _ in range(m)]
    print(ans)

    for i in range(m):
        for j in range(n):
            if mat[i][j] == 0:
                ans[i][j] = 0
            else:
                left = ans[i][j-1] if j > 0 else sys.maxsize
                up = ans[i-1][j] if i > 0 else sys.maxsize
                ans[i][j] = min(left,up) + 1

    print(ans)
    for i in range(m-1,-1,-1):
        for j in range(n-1,-1,-1):
            if mat[i][j] == 0:
                ans[i][j] = 0
            else:
                right = ans[i][j+1] if j < n-1 else sys.maxsize
                down = ans[i+1][j] if i < m - 1 else sys.maxsize
                ans[i][j] = min(ans[i][j] , min(right,down) + 1)
    return ans

if __name__ == '__main__':
    print(update_matrix([[0,1,1],[1,1,1],[1,1,1]]))
