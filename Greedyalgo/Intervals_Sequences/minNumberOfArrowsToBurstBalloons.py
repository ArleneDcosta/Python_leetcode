from typing import List

def findMinArrowShots( points: List[List[int]]) -> int:
    if not points:
        return 0
    ans  = 1
    points.sort(key = lambda x: x[1])
    print(points)
    curr_end = points[0][1]
    for i in range(0,len(points)):
        if points[i][0] > curr_end:
            ans += 1
            curr_end = points[i][1]

    return ans

if __name__ == '__main__':
    print(findMinArrowShots([[10,16],[2,8],[1,6],[7,12]]))
    print(findMinArrowShots([[1,2],[3,4],[5,6],[7,8]]))