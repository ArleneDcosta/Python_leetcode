from typing import List
from collections import deque

#BFS
def minDays(n:int) -> int:
    def dp(n):
        if n in memo:
            return memo[n]
        if n == 0:
            return 0

        if n == 1:
            return 1
        # Handling the dp(i-1) case to reach n//3 you have to eliminate n % 3
        ans = 1 + min(n % 3 + dp(n//3), n % 2 + dp(n//2))
        # Here 1 signifies the current case and the min dp signifies the previous cases

        memo[n] = ans
        return ans

    memo = {}
    return dp(n)

if __name__ == '__main__':
    print(minDays(10))