from typing import List
from collections import Counter

def reorganizeString(s: str) -> str:
    N = len(s)
    A = []
    for c, x in sorted((s.count(x), x) for x in set(s)):
        if c > (N+1)/2: return ""
        A.extend(c * x)
    print(A)
    ans = [None] * N
    ans[::2], ans[1::2] = A[N//2:], A[:N//2]
    return "".join(ans)
        
        
if __name__ == '__main__':
    print(reorganizeString("aabcc"))