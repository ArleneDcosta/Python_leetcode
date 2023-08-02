def solve(A):
    absoluteMax = A[0]
    localMax =A[0]
    nextSum = 0
    
    for i in range(1,len(A)):
        nextSum = localMax + A[i]
        localMax = max(A[i],nextSum)
        absoluteMax = max(localMax,absoluteMax)
    return absoluteMax


print solve([-2,-3, 4, -1, -2, 1, 5, -3])
