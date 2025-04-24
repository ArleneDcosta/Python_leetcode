from collections import defaultdict,deque
from typing import List

def numOfMinutes(n: int, headID: int, manager: List[int], informTime: List[int]) -> int:
    g = defaultdict(list)

    for i in range(len(manager)):
        if manager[i] != -1:
            g[manager[i]].append(i)

    queue = []
    queue.append(headID)

    def dfs(node):
        if len(g[node]) == 0:
            return informTime[node]
        currentlist = []
        for val in g[node]:
            currentlist.append(dfs(val) + informTime[node])

        return max(currentlist)

    return dfs(headID)

def numOfMinutesOp( n: int, headID: int, manager: List[int], informTime: List[int]) -> int:
    manager_to_direct_reports = defaultdict(list)

    for direct_report, manager in enumerate(manager):
        manager_to_direct_reports[manager].append(direct_report)
    
    q = deque()
    q.append((headID, 0))
    numMinutes = 0

    while q:
        manager, minutesSoFar = q.popleft()
        numMinutes = max(numMinutes, minutesSoFar)

        # if manager is not a manager then he will tell no one
        for direct_report in manager_to_direct_reports[manager]:
            q.append((direct_report, minutesSoFar + informTime[manager]))
    
    return numMinutes

def numOfMinutesSOp(self, n: int, headID: int, manager: List[int], informTime: List[int]) -> int:
        
        def find(i):
            if manager[i] != -1:
                informTime[i] += find(manager[i])
                manager[i] = -1
            return informTime[i]
            
        return max(map(find, range(n)))

if __name__ == '__main__':
    n = 6
    headID = 2
    manager = [2,2,-1,2,2,2]
    informTime = [0,0,1,0,0,0]
    print(numOfMinutes(n,headID,manager,informTime))


    n = 1
    headID = 0
    manager = [-1]
    informTime = [0]
    print(numOfMinutes(n,headID,manager,informTime))

    n = 15
    headID = 0
    manager = [-1,0,0,1,1,2,2,3,3,4,4,5,5,6,6]
    informTime = [1,1,1,1,1,1,1,0,0,0,0,0,0,0,0]
    print(numOfMinutes(n,headID,manager,informTime))