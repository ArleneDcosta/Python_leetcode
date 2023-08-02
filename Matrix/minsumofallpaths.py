def solve(A,i,j,l,sum):
    #print i,j
    if i == (len(A)-1) and j == (len(A[0])-1):
        sum+=A[len(A)-1][len(A[0])-1]
        l.append(sum)

    sum +=A[i][j]
    if i < (len(A)-1):
        l = solve(A,i+1,j,l,sum)
        
    if j < (len(A[0])-1):
        l = solve(A,i,j+1,l,sum)

    return l

sum = 0
A=[[1,3,1],[1,5,1],[4,2,1]]
print(solve(A,0,0,[],sum))
A = [[1,2,3,1],[4,5,6,7],[1,1,1,1]]
print(solve(A,0,0,[],0))
