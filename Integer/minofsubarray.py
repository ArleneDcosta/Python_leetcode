def sumSubarrayMins(A):
    MOD = 10**9 + 7
    N = len(A)

    # prev has i* - 1 in increasing order of A[i* - 1]
    # where i* is the answer to query j
    stack = []
    prev = [None] * N
    print A
    for i in xrange(N):
        while stack and A[i] <= A[stack[-1]]:
            stack.pop()
        prev[i] = stack[-1] if stack else -1
        print 'prev',prev
        stack.append(i)
        print 'stack',stack

    # next has k* + 1 in increasing order of A[k* + 1]
    # where k* is the answer to query j
    stack = []
    next_ = [None] * N
    for k in xrange(N-1, -1, -1):
        while stack and A[k] < A[stack[-1]]:
            stack.pop()
        next_[k] = stack[-1] if stack else N
        print 'next_',next_
        stack.append(k)
        print 'stack2',stack
    print prev
    print next_
    
    for i in xrange(N):
        print 'Final Inside'
        print (i - prev[i]),
        print (next_[i] - i),
        print A[i]
    # Use prev/next array to count answer
    return sum((i - prev[i]) * (next_[i] - i) * A[i] for i in xrange(N)) % MOD
    #here prev is the highest possible value that can be obtained as compared to subarray backward elements[degree of greatest]
    #here next is the highest possible value that can be otained as compared to subarray forward elements[gegree of greatest]
    #subtracting with the index obtains the smallest
print sumSubarrayMins([3,1,2,4])
'''
Input: [3,1,2,4]
Output: 17
Explanation: Subarrays are [3], [1], [2], [4], [3,1], [1,2], [2,4], [3,1,2], [1,2,4], [3,1,2,4]. 
Minimums are 3, 1, 2, 4, 1, 1, 2, 1, 1, 1.  Sum is 17.
'''
