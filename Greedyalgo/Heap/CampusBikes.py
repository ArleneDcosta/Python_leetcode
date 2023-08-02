from typing import List
from heapq import heapify,heappush,heappop

def assignedBikes(workers:List[List[int]],bikes:List[List[int]]) -> List[int]:
    distance = []
    for i,(wx,wy) in enumerate(workers):
        bike_distance = []
        for j,(bx,by) in enumerate(bikes):
            bike_distance.append((abs(wx-bx)+abs(wy-by),i,j))
        bike_distance.sort()
        distance.append(bike_distance)
    print(distance)
    pq = [d.pop(0) for d in distance]
    heapify(pq)
    print(pq)

    ans = [None] * len(workers)
    assigned_bike = set()
    while len(assigned_bike) < len(workers):
        dist,worker,bike = heappop(pq)
        print(dist,worker,bike)
        if bike not in assigned_bike:
            ans[worker] = bike
            assigned_bike.add(bike)
        else:
            next_shortest_bike = distance[worker].pop()
            heappush(pq,next_shortest_bike)
    return ans

if __name__ == '__main__':
    print(assignedBikes([[0,0],[2,1]],[[1,2],[3,3]]))