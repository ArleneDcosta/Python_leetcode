def solveSudoku(g):
    row = [[1]*9 for i in range(9)]        
    col = [[1]*9 for i in range(9)]
    sib = [[1]*9 for i in range(9)]  # 3*3 sub-box, from left to right, top to bottom.
    to_add = []
    for i in range(9):
        for j in range(9):
            #print(i,j)
            if g[i][j] != '.':
                d = int(g[i][j]) - 1
                #print(i//3*3+j//3,i,j,d)
                row[i][d] = col[j][d] = sib[i//3*3+j//3][d] = 0
            else:
                to_add.append((i, j))
    #print row
    #print col
    #print sib
    #print to_add
    #start stack at -1 as we are 0 indexing the suduko board to make indexing easier
    stack = [-1]
    while len(stack) <= len(to_add):
        #print(stack)
        stack[-1]+=1
        d = stack[-1]
        i,j = to_add[len(stack)-1]
            
        if d > 8:  
            # if it is not possible to fill square commence backtracking
            stack.pop()
            d1 = stack[-1] # backtrack and reset descisions from last
            i1,j1 = to_add[len(stack)-1]
            row[i1][d1] = col[j1][d1] = sib[i1//3*3+j1//3][d1] = 1
                 
        elif row[i][d] and col[j][d] and sib[i//3*3+j//3][d]:
            # if the chosen value is valid go to next square
            row[i][d] = col[j][d] = sib[i//3*3+j//3][d] = 0
            stack.append(-1)
        
		#apply changes
    print(stack)
    dc = {to_add[i]:stack[i] for i in range(len(to_add))}
    print dc
    for c1,r in enumerate(g):
        for c2,c in enumerate(r):
            if c == '.':
                g[c1][c2] = str(dc[(c1,c2)]+1)
    return g

print solveSudoku([["5","3",".",".","7",".",".",".","."],["6",".",".","1","9","5",".",".","."],[".","9","8",".",".",".",".","6","."],["8",".",".",".","6",".",".",".","3"],["4",".",".","8",".","3",".",".","1"],["7",".",".",".","2",".",".",".","6"],[".","6",".",".",".",".","2","8","."],[".",".",".","4","1","9",".",".","5"],[".",".",".",".","8",".",".","7","9"]])
