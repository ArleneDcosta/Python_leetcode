import copy
def solveNQueens(n):
    result = []
    #queens : aldready added queens
    #start_i : row position for a new queen
    #start_j : col postion for a new queen
    def checkDiagonal(queens, start_i, start_j):
        iteration = 1
	# move by 1 to the top-left and top-right with checking already placed queens
        for i in range(start_i-1, -1, -1):
	    # is any queen on our path to the top?
            if queens[i] in [start_j - iteration, start_j + iteration]:
                return False
            iteration += 1
        return True
                
    def solve(queens):
        # all queens in the list - add to the solution
        if len(queens) == n:
            result.append(["."*i+'Q'+"."*(n-i-1) for i in queens])
        # we are moving from top to bottom, 
        # so the next row index equals number of already added queens (last queen index + 1)
        row = len(queens)
	# iterate columns
        print(row)
        for j in range(n):
            # discard if queen already placed to the column j
            if j in queens:
                continue
            if not queens or checkDiagonal(queens, row, j):
                new_queens = copy.deepcopy(queens)
                print(queens, row, j)
                new_queens.append(j)
                print(queens)
                solve(new_queens)
        
    solve([])
    return result

print(solveNQueens(4))
