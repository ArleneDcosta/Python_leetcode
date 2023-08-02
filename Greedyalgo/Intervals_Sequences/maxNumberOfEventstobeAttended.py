from typing import List
from heapq import heappop,heappush

def maxEvents(events: List[List[int]]) -> int:
    events.sort(key = lambda x : x[0])
    total_days =  max(event[1] for event in events)
    print(events,total_days)

    day = 0
    pq = []
    ans = 0
    index = 0
    while day <= total_days:
        # add to progress
        while index < len(events) and events[index][0] <= day:
            heappush(pq,events[index][1])
            print(pq,day)
            index += 1

        #Discard prev events when multiple events started and ended before specific days
        while pq and pq[0] < day:
            heappop(pq)
            print('After heappop',pq)

        if pq:
            heappop(pq)
            ans += 1
        day += 1

    return ans


if __name__ == '__main__':
    print(maxEvents([[1,2],[1,2],[1,6],[1,2],[1,2]]))
    print(maxEvents([[1,2],[2,3],[3,4],[1,2]]))