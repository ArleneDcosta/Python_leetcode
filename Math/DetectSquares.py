from typing import List
from collections import defaultdict,Counter
class DetectSquares:
    #Here Counter is similiar to defaultdict as it doesnt require keys but initialises to default 0 values for missing keys
    def __init__(self):
        self.pointsPerY = defaultdict(Counter)

    def add(self, point: List[int]) -> None:
        x,y = point
        self.pointsPerY[y][x] += 1
        print(self.pointsPerY)

    def count(self, point: List[int]) -> int:
        x1,y = point
        points  = self.pointsPerY[y]
        ans = 0
        #print(points)
        for x2 in points.keys():
            if x1 != x2:
                ans += self.pointsPerY[y][x2] * self.pointsPerY[y+abs(x2 - x1)][x1] * self.pointsPerY[y+abs(x2 - x1)][x2]
                #print(self.pointsPerY[y][x2],self.pointsPerY[y - abs(x2 - x1)][x1])
                ans += self.pointsPerY[y][x2] * self.pointsPerY[y - abs(x2 - x1)][x1] * self.pointsPerY[y - abs(x2 - x1)][x2]
        return ans

if __name__ == '__main__':
    # Your DetectSquares object will be instantiated and called as such:
    obj = DetectSquares()
    command = [ "add", "add", "add", "count", "count", "add","add", "count"]
    points  = [[3, 10], [11, 2], [3, 2], [11, 10], [14, 8], [11, 2], [11, 10],[11,10]]
    for i in range(0,len(points)):
        if command[i] == 'add':
            obj.add(points[i])
        else:
            print(obj.count(points[i]))
    # param_2 = obj.count(point)