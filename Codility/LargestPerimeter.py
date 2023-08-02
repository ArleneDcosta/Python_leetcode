def largestPerimeter(A):
    A.sort()
    for i in xrange(len(A) - 3, -1, -1):
        if A[i] + A[i+1] > A[i+2]:
            return A[i] + A[i+1] + A[i+2]
    return 0


print largestPerimeter([2,1,2])
print largestPerimeter([])
