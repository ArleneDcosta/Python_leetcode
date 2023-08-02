def solve(A):
    for i in range(0,len(A)):
        for j in range(0,i):
            A[i][j],A[j][i] = A[j][i],A[i][j]
    for i in range(0,len(A)):
        for j in range(0,len(A[0])):
            print A[i][j],
        print 
solve([[1,2,3],[4,5,6],[7,8,9]])
