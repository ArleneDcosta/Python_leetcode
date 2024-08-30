from typing import List
#https://leetcode.com/problems/minimum-initial-energy-to-finish-tasks/description/
def minimumEffort(tasks: List[List[int]]) -> int:
    tasks = sorted(tasks, key=lambda x: x[1] - x[0], reverse=True)
    def helper(mid):
        for a,m in tasks:
            if mid < m:
                return False
            mid -= a
        return True

    left = sum([a for a,m in tasks])
    right = sum([m for a, m in tasks])
    while(left < right):
        mid = left + (right - left) // 2
        print(mid)
        # Since minimum is asked right = mid
        if helper(mid):
            right = mid

        else:
            left =  mid + 1
    return left


if __name__ == '__main__':
    print(minimumEffort([[1,2],[2,4],[4,8]]))
    # print(minimumEffort([[1,3],[2,4],[10,11],[10,12],[8,9]]))