from collections import defaultdict

def canFinish(numCourses, prerequisites):
    pre = defaultdict(list)
    for course, p in prerequisites:
        pre[course].append(p)
    taken = set()

    def dfs(course):
        #There is no prerequisite
        print(taken)
        if not pre[course]:
            return True
        if course in taken:
            return False
        taken.add(course)
        for p in pre[course]:
            if not dfs(p): return False
        pre[course] = []
        return True

    for course in range(numCourses):
        if not dfs(course):
            return False

    return True

if __name__ == '__main__':
    # print(canFinish(numCourses = 2, prerequisites = [[1,0],[0,1]]))
    # print(canFinish(numCourses = 2, prerequisites = [[1,0]]))
    # print(canFinish(2,[[0,1],[1,0]]))
    # print(canFinish(20,[[0,10],[3,18],[5,5],[6,11],[11,14],[13,1],[15,1],[17,4]]))
    print(canFinish(5,[[1,4],[2,4],[3,1],[3,2]]))