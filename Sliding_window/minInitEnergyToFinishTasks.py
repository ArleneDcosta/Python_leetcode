from typing import List

def minimumEffort(tasks: List[List[int]]) -> int:
    maxele = -10000
    for i in range(0,len(tasks)):
        if tasks[i][1] > maxele:
            maxele = tasks[i][1]
    tasks = sorted(tasks, key=lambda x: x[1] - x[0], reverse=True)
    print(tasks)
    ans = 0
    cur_saved = 0
    for a,minimum in tasks:
        if minimum > cur_saved:
            needed = minimum - cur_saved
            print(minimum,needed,cur_saved,ans)
            ans += needed
            cur_saved += needed

        cur_saved -= a

    return ans

if __name__ == '__main__':
    # print(minimumEffort([[1,2],[2,4],[4,8]]))
    print(minimumEffort([[1,3],[2,4],[10,11],[10,12],[8,9]]))