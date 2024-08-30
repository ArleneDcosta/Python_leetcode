from typing import List
from math import gcd

def solve(a, b, x, y):
    if gcd(x, y) == gcd(a, b):
        print("YES")
    else:
        print("NO")
    # Write your code here

def isPossible(a:int,b:int,c:int,d:int,dp:List[List[int]]) -> int:
    print(a,b,c,d)
    if dp[a][b]!=-1:
        return dp[a][b]

    if a == c and b == d:
        dp[a][b] = 'Yes'
    elif a > c or b > d:
        dp[a][b] = 'No'
    else:
        dp[a][b] = 'No'
        if a < c:
            if isPossible(a+b,b,c,d,dp) == 'Yes':
                dp[a][b] = 'Yes'
        if b < d:
            if isPossible(a,b+a,c,d,dp) == 'Yes':
                dp[a][b] = 'Yes'

    return dp[a][b]

if __name__ == '__main__':
    a = 36
    b = 6
    c = 78
    d = 36
    print(solve(a,b,c,d))
    print(gcd(78,36),gcd(36,6))