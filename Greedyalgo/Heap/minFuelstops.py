from typing import List
from heapq import heappop,heappush

def minRefuelStops(target: int, startFuel: int, stations: List[List[int]]) -> int:
    pq = []
    ans = 0
    n = len(stations)
    i = 0
    cur = startFuel
    while cur < target:
        while i < n and stations[i][0] <= cur:
            heappush(pq,- stations[i][1])
            i+=1
        print(pq)
        if not pq:
            return -1

        cur += - heappop(pq)
        ans +=1

    return ans

if __name__ == '__main__':
    print(minRefuelStops(target = 100, startFuel = 90, stations = [[10,60],[20,30],[30,30],[60,40]]))
