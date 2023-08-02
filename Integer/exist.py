def exist(board, word) :
        
    row, col = len(board), len(board[0])
        
    def dfs(r, c, i):
        # If we are looking for the last letter (this means that it has been already found)
        if i == len(word) - 1 :
            return True 
 
        original = board[r][c]
    
        # Mark the board so its not visited again in next recursive call
        board[r][c] = "#"
            
        # Visit 4 directions of current cell  
        for dx, dy in [[-1,0], [1,0], [0,-1],[0,1]]:
            dr = r + dy
            dc = c + dx
                
            # If the next tile in is the graph and equal to next letter 
            if 0 <= dr < row and 0 <= dc < col and board[dr][dc] == word[i + 1]:
                if dfs(dr, dc, i + 1):
                    return True 
                    
        # Unmark the board so the previous recursive calls can use it
        board[r][c] = original
        
    #Finding first letter                    
    for r in range(row):
        for c in range(col): 
                
            # Searching for index (letter) in word 
            i = 0 
                
            # Find first letter of word 
            if board[r][c] == word[0]:
                if dfs(r, c, i):
                    return True 
    return False
print exist(board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "ABCCED")
