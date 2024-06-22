from typing import List
import sys
#Almost similiar to maxdisjoint intervals
def deleteIntervals( points: List[List[int]]) -> int:
    if not points:
        return 0
    ans  = 0
    points.sort(key = lambda x: x[1])
    print(points)
    curr_end = -sys.maxsize
    for i in range(0,len(points)):
        if points[i][0] >= curr_end:
            curr_end = points[i][1]
        else:
            ans += 1

    return ans

if __name__ == '__main__':
    print(deleteIntervals([[10,16],[2,8],[1,6],[7,12]]))
    print(deleteIntervals([[1,2],[3,4],[5,6],[7,8]]))