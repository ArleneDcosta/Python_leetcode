from typing import List
from collections import deque

#BFS
def minDays(n:int) -> int:
    queue = deque([n])
    seen  = set()
    seen.add(n)
    ans = 0

    while queue:
        for _ in range(len(queue)):
            cur_n = queue.popleft()

            if cur_n == 0:
                return ans
            # Remaining oranges left
            if cur_n % 3 == 0 and cur_n//3 not in seen:
                queue.append(cur_n//3)
                seen.add(cur_n//3)
            if cur_n % 2 == 0 and cur_n//2 not in seen:
                queue.append(cur_n//2)
                seen.add(cur_n//2)

            if cur_n - 1 not in seen:
                queue.append(cur_n - 1)
                seen.add(cur_n - 1)
        ans += 1
    return -1

if __name__ == '__main__':
    print(minDays(10))