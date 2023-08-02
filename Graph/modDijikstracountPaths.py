#Dijikstra find shortest path from one node[src] to all nodes with weighted paths[ Works for both directed and non-directed].

# Here when we get better path we need to reset the algorithm
import sys
from typing import List
from collections import defaultdict
from heapq import heappop,heappush

def countPaths(n: int, roads: List[List[int]]) -> int:
    graph = defaultdict(list)
    for u,v,t in roads:
        graph[u].append((v,t))
        graph[v].append((u,t))
        #since birrectional should do both ways
    print(graph)
    #initialization
    times = [sys.maxsize ] * n
    times[0] = 0

    ways = [0] * n
    ways[0] = 1
    pq = [(0,0)] #base case
    while pq:
        print(pq)
        #Removal of min node
        #If u dont add min value then the cycle will unnecessarily increase as the same node will be added in the queue
        old_t,u = heappop(pq)
        for v,t in graph[u]:
            new_t = old_t + t

            if new_t < times[v]:
                heappush(pq,(new_t,v)) #decreasekey
                times[v] = new_t
                ways[v] = ways[u]
            #Additional information
            elif new_t == times[v]:
                ways[v] += ways[u]
    mod = 10**9 + 7

    print(times,pq,ways)
    return ways[-1] % mod

if __name__ == '__main__':
    print(countPaths(7,[[0,6,7],[0,1,2],[1,2,3],[1,3,3],[6,3,3],[3,5,1],[6,5,1],[2,5,1],[0,4,5],[4,6,2]]))


