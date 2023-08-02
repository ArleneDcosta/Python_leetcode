def sumSubseqWidths(A):
    MOD = 10**9 + 7
    N = len(A)
    A.sort()

    pow2 = [1]
    for i in xrange(1, N):
        pow2.append(pow2[-1] * 2 % MOD)

    ans = 0
    print pow2
    for i, x in enumerate(A):
        print i,x
        ans = (ans + (pow2[i] - pow2[N-1-i]) * x) % MOD
    return ans



print sumSubseqWidths([2,3,1])
'''
Input: [2,1,3]
Output: 6
Explanation:
Subsequences are [1], [2], [3], [2,1], [2,3], [1,3], [2,1,3].
The corresponding widths are 0, 0, 0, 1, 1, 2, 2.
The sum of these widths is 6.'''
