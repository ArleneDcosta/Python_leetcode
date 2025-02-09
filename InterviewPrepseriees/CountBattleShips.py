from typing import List



def countBattleships(board: List[List[str]]) -> int:
    rows = len(board)
    cols = len(board[0])
    def dfs(i,j):
        if i > rows - 1 or j > cols - 1 or board[i][j] == ".":
            return True
        
        if dfs(i+1,j):
            if j+1 < cols and board[i][j+1] == 'X':
                return False
            if i+1 < rows:
                board[i+1][j] = '.' 
            
        if dfs(i,j+1):
            if i + 1 < rows and board[i+1][j] == "X":
                return False
            if j+1 < cols:
                board[i][j+1] = '.'

        return True
    
    res = 0
    for i in range(0,rows):
        for j in range(0,cols):
            if board[i][j] == "X":
                if dfs(i,j):
                    res += 1

    return res

def countBattleshipsoptimizeds(board):
        count = 0
        for r in range(len(board)):
            for c in range(len(board[r])):
                if board[r][c] != 'X': continue
                if r > 0 and board[r-1][c] == 'X': continue
                if c > 0 and board[r][c-1] == 'X': continue
                count += 1
        return count

if __name__ == '__main__':
    board = [["X",".",".","X"],[".",".",".","X"],[".",".",".","X"]]
    print(countBattleships(board))

    board = [["."]]
    print(countBattleships(board))