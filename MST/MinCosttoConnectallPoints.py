from typing import List

#Greedy algo works like MST


def minCostConnectPoints(points: List[List[int]]) -> int:
    # Initialize with the first point
    n = len(points)
    parents  = list(range(n))
    print(parents)
    ranks = [0] * n

    def find(x):
        #Keep finding till the ancestors of both the curr and prev value dont match
        if parents[x] != x:
            parents[x] = find(parents[x])
        return parents[x]

    def union(x,y):
        r1 = find(x)
        r2 = find(y)
        if r1 != r2:
            #create an edge as there is no prexisting edge and ancestor for the nodes
            parents[r2] = r1
            return True
        else:
            #dont create an edge as there is a prexisting edge
            return False

    def getDist(p1,p2):
        return abs(p1[0] - p2[0]) + abs(p1[1] - p2[1])

    paths = []
    for i in range(n):
        for j in range(i+1,n):
            dist = getDist(points[i],points[j])
            paths.append((dist,i,j))
    paths.sort()
    print(paths)
    ans = 0
    for dist,p1,p2 in paths:
        print(p1,p2,parents)
        if union(p1,p2):
            ans += dist
    return ans
    #Check if there is aldready an edge preexisting
    #
if __name__ == '__main__':
    print(minCostConnectPoints([[0,0],[2,2],[3,10],[5,2],[7,0]]))