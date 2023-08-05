from typing import List
from heapq import heappush,heappop
def maxPerformance(n: int, speed: List[int], efficiency: List[int], k: int) -> int:
    MOD =  10 ** 9 + 7

    ans = 0
    curr_total_speed = 0
    pq = []

    for e,s in sorted(zip(efficiency,speed),reverse=True):
        print(e,s)
        heappush(pq,s)
        print(pq)
        curr_total_speed += s

        if len(pq) > k:
            curr_total_speed -= heappop(pq)
        ans =  max(ans,curr_total_speed * e)

    return ans % MOD

if __name__ == '__main__':
    print(maxPerformance(6,[2,10,3,1,5,8],[5,4,3,9,7,2],3))