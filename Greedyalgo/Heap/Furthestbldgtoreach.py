from typing import List
from heapq import heappop,heappush,heapify

#This for loop always chooses bricks so will fail
# if you use DP it will TLE due to different combinations
# Check where max difference is observed there use a ladder
# also flaw is bricks should not be equal to 0 the bricks should not suffice to match the current building
# The issue is that when we choose ladder then return the bricks
def furthestBuilding(heights: List[int], bricks: int, ladders: int) -> int:
    '''for i in range(1,len(heights)):
        if heights[i] > heights[i-1]:
            if bricks == 0 and ladders == 0:
                return i-1
            if (heights[i] - heights[i-1]) <= bricks and bricks > 0:
                bricks -= (heights[i] - heights[i-1])
            else:
                ladders -= 1
    return i'''
    pq = []
    total_bricks = 0
    n = len(heights)
    ans  = 0
    for i in range(0,n-1):
        diff = heights[i+1] - heights[i]
        if diff <= 0:
            continue
        total_bricks += diff
        heappush(pq,-diff)
        if total_bricks > bricks:
            if ladders == 0:
                return i
            else:
                ladders -= 1
                total_bricks += heappop(pq)
    return n - 1

if __name__ == '__main__':
    print(furthestBuilding(heights = [4,12,2,7,3,18,20,3,19], bricks = 10, ladders = 2))
    print(furthestBuilding(heights = [14,3,19,3], bricks = 17, ladders = 0))
    print(furthestBuilding(heights = [4,2,7,6,9,14,12], bricks = 5, ladders = 1))
    print(furthestBuilding(heights = [1,5,1,2,3,4], bricks = 4, ladders = 1))