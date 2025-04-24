
from typing import List
from collections import deque
import sys

def coinChange(coins: List[int], amount: int) -> int:
    if amount == 0:
        return 0

    visited = set()
    queue = deque([(0, 0)])  # (current_sum, steps)

    while queue:
        curr_sum, steps = queue.popleft()
        for coin in coins:
            next_sum = curr_sum + coin
            if next_sum == amount:
                return steps + 1
            if next_sum < amount and next_sum not in visited:
                visited.add(next_sum)
                queue.append((next_sum, steps + 1))

    return -1

def coinChange_dp(coins: List[int], amount: int) -> int:
        dp = [amount + 1] * (amount + 1)
        dp[0] = 0 

        for i in range(1, amount + 1):
            for coin in coins:
                if i - coin >= 0:
                    dp[i] = min(dp[i], dp[i - coin] + 1)

        return dp[amount] if dp[amount] <= amount else -1

if __name__ == '__main__':
    coins = [1,2,5]
    amount = 11
    print(coinChange(coins,amount))

    coins = [2]
    amount = 3
    print(coinChange(coins,amount))

    coins = [1]
    amount = 1
    print(coinChange(coins,amount))