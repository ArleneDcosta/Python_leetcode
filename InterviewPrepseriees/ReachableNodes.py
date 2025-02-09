from typing import List
from collections import defaultdict
import sys
from heapq import heappop,heappush,heapify

def reachableNodes(edges: List[List[int]], maxMoves: int, n: int) -> int:
    graph = defaultdict(list)
    for u,v, weight in edges:
        graph[u].append((v,weight+1))
        graph[v].append((u,weight+1))

    dist = [sys.maxsize] * n
    dist[0] = 0

    pq = [(0,0)]
    while pq:
        d,u = heappop(pq)
        for v,nd in graph[u]:
            if d + nd < dist[v]:
                dist[v] = d + nd
                heappush(pq,(d+nd,v))
    
    ans = 0
    for u,v in enumerate(dist):
        if dist[u] <= maxMoves:
            ans += 1
    print(dist)
    for u,v,w in edges:
        if dist[u] > maxMoves and dist[u] > maxMoves:
            continue
        cnt1 = max(maxMoves -  dist[u],0)
        cnt2 = max(maxMoves -  dist[v],0)
        ans += min(cnt1 + cnt2, w)

    return ans

if __name__ == '__main__':
    edges = [[0,1,10],[0,2,1],[1,2,2]]
    maxMoves = 6
    n = 3
    print(reachableNodes(edges,maxMoves,n))

    edges = [[0,1,4],[1,2,6],[0,2,8],[1,3,1]]
    maxMoves = 10
    n = 4
    print(reachableNodes(edges,maxMoves,n))