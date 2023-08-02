def solve(A):
    A.sort()
    if (A[0]-1)*(A[1]-1) > (A[-1]-1)*(A[-2]-1):
        return (A[0]-1)*(A[1]-1)
    return (A[-1]-1)*(A[-2]-1)


print solve([3,4,5,2])

print solve([1,5,4,5])

        
