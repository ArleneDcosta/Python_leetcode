def getBoxIdx(i, j):
    return (i//3)*3 + (j // 3)
    
def isValidSudoku(board):
    '''rows = [set() for _ in range(9)]
    cols = [set() for _ in range(9)]
    boxes = [set() for _ in range(9)]
    print rows
    for i, row in enumerate(board):
        for j, num in enumerate(row):
            print "i:",i,"row",row,"j",j,"num",num,"boxidx",(i//3)*3 + (j // 3)
            if num.isdigit():
                # check for duplicates in row
                if num in rows[i]:
                    return False
                rows[i].add(num)

                    # check for duplicates in column
                if num in cols[j]:
                    return False
                cols[j].add(num)

                    # check for duplicates in sub-box
                boxIdx = getBoxIdx(i, j)
                if num in boxes[boxIdx]:
                    return False
                boxes[boxIdx].add(num)'''
    row = [[1]*9 for i in range(9)]        
    col = [[1]*9 for i in range(9)]
    sib = [[1]*9 for i in range(9)]  # 3*3 sub-box, from left to right, top to bottom.

    for i in range(9):
        for j in range(9):
            #print(i,j)
            if board[i][j] != '.':
                d = int(g[i][j]) - 1
                #print(i//3*3+j//3,i,j,d)
                if row[i][d] and col[j][d] and sib[i//3*3+j//3][d]:
                    row[i][d] = col[j][d] = sib[i//3*3+j//3][d] = 0
                else:
                    return False
        
  
    return True
print isValidSudoku([["5","3",".",".","7",".",".",".","."],["6",".",".","1","9","5",".",".","."],[".","9","8",".",".",".",".","6","."],["8",".",".",".","6",".",".",".","3"],["4",".",".","8",".","3",".",".","1"],["7",".",".",".","2",".",".",".","6"],[".","6",".",".",".",".","2","8","."],[".",".",".","4","1","9",".",".","5"],[".",".",".",".","8",".",".","7","9"]])
