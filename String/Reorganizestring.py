def reorganizeString(S):
    N = len(S)
    A = []
    for c, x in sorted((S.count(x), x) for x in set(S)):
        if c > (N+1)/2: return ""
        A.extend(c * x)
    ans = [None] * N
    print A,ans[::2], ans[1::2]
    ans[::2], ans[1::2] = A[N/2:], A[:N/2]
    print ans[::2], ans[1::2],ans
    return "".join(ans)
print reorganizeString("aab")
