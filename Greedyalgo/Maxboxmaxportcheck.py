import sys
from typing import List

def boxDelivering(boxes: List[List[int]], portsCount: int, maxBoxes: int, maxWeight: int) -> int:
    n = len(boxes)
    dp = [sys.maxsize] * (n+1)
    dp[0] = 0
    weight = 0
    trips = 2 # Take weight from storage to port and from port back to storage
    #Sliding window approach
    left = 0
    for right in range(n):
        print(right,dp)
        weight += boxes[right][1]
        # Ports are different
        # If current box is different than prev trip then need to do one more trip
        if right > 0 and boxes[right][0] != boxes[right-1][0]:
            trips += 1

        while(right - left >= maxBoxes or weight > maxWeight or (left < right and dp[left] == dp[left + 1])):
            print('LEFT',left,trips)
            weight -= boxes[left][1]
            if (boxes[left][0] != boxes[left+1][0]):
                trips -= 1
            left += 1
        dp[right + 1] = dp[left] + trips

    return dp[-1]

'''
For dp the dp[i] =  dp [k] + trips( will contain different constraints i.e maxweight and maxboxcount)
To find it via dp will take O(n^2) complexity which will fail
Hence we need to solve this problem via Greedy approach
'''

if __name__ == '__main__':
    # print(boxDelivering(boxes = [[2,4],[2,5],[3,1],[3,2],[3,7],[3,1],[4,4],[1,3],[5,2]],portsCount = 5,maxBoxes = 5, maxWeight = 7))
    # print(boxDelivering(boxes = [[1,2],[3,3],[3,1],[3,1],[2,4]], portsCount = 3, maxBoxes = 3, maxWeight = 6))
    # print(boxDelivering(boxes = [[1,1],[2,1],[1,1]], portsCount = 2, maxBoxes = 3, maxWeight = 3))
    # print(boxDelivering(boxes = [[1,4],[1,2],[2,1],[2,1],[3,2],[3,4]], portsCount = 3, maxBoxes = 6, maxWeight = 7))
    print(boxDelivering(boxes=[[1, 4], [1, 2], [2, 1],[2,1]], portsCount=3, maxBoxes=6, maxWeight=7))
