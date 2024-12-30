
from collections import defaultdict

def canFinish(numCourses, prerequisites):
    pre = defaultdict(list)
    for course, p in prerequisites:
        pre[course].append(p)
    taken = set()

    def dfs(course):
        if not pre[course]:
            return True
        if course in taken:
            return False
        taken.add(course)
        for p in pre[course]:
            if not dfs(p): 
                return False
        pre[course] = []
        return True
    
    for course in range(numCourses):
        if not dfs(course):
            return False

        return True
    

if __name__ == '__main__':
    print(canFinish(2,[[1,4],[2,4],[3,1],[3,2]]))