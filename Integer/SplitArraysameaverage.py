def splitArraySameAverage(A):
    total = sum(A)
    print total
        # The ans does not change if we scale or shift the array
    for i in range(len(A)): A[i] = len(A) * A[i] - total
        # The above ensures that sum(A)=Avg(A)=avg(B)=avg(C)=sum(B)=sum(C)=0
        # So we are looking for a non-empty strict subset of A that sum to 0
    print A
    A.sort() #help prune the search a bit
    X = set()
    for a in A[:-1]: #excluding last element so it looks for STRICT subset or else will be looking for sum of the entire array which will make no sense
        print a
        X |= { a } | { a + x for x in X if x < 0}
        print X
        if 0 in X: return True
    return False


print splitArraySameAverage([1,2,3,4,5,6,7])
#print splitArraySameAverage([1,3,4,5,7])
#print splitArraySameAverage([1,3,4,6,7])
#4 + 1 + 7=12/3=4 and 5+3/2=4 so thats how the algo is designed
