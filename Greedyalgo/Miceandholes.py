def mice(A,B):
    A.sort()
    B.sort()
    ans = 0
    for a,b in zip(A,B):
        ans = max(ans, abs(a-b))
    return ans


print(mice())
