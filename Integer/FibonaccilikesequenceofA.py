def lenLongestFibSubseq(A):
    S = set(A)
    ans = 0
    for i in xrange(len(A)):
        for j in xrange(i+1, len(A)):
            """
            With the starting pair (A[i], A[j]),
            y represents the future expected value in
            the fibonacci subsequence, and x represents
            the most current value found.
            """
            x, y = A[j], A[i] + A[j]
            length = 2
            while y in S:
                x, y = y, x + y
                length += 1
            ans = max(ans, length)
    return ans if ans >= 3 else 0

print lenLongestFibSubSeq([1,2,3,4,5,6,7,8])
