from typing import List
import sys

def minSessions(tasks: List[int], sessionTime: int) -> int:
    def dp(mask,session):
        if mask == 0 :
            return 0
        ans =  sys.maxsize
        for i in range(len(tasks)):
            #IF 1 then unused
            if mask & (1<<i) != 0:
                if tasks[i] <= session:
                    ans =  min(ans,dp( mask ^ (1 << i),session - tasks[i]))
                    #Same thing opposite the xor will get replaced by or 0 to 1 or and  1 to 0 xor
                else:
                    ans = min(ans, 1 + dp(mask ^ (1 << i), sessionTime - tasks[i]))


        return ans
    n = len(tasks)
    return dp((1<<n)-1,0)

def minSessionsoptimized(tasks: List[int], sessionTime: int) -> int:

    def dp(mask):
        if mask == 0 :
            return 0,0
        ans =  sys.maxsize
        remainTime = 0 # settinng as worst as ans is set
        for i in range(len(tasks)):
            if mask & (1<<i) != 0:
                ans1,remainTime1 = dp( mask ^ (1 << i))
                if tasks[i] <= remainTime1:
                    remainTime1 -= tasks[i]
                else:
                    ans1 += 1
                    remainTime1 = sessionTime - tasks[i]
        #check if there is improvement in ans and remaintime or just remaintime
                if ans1 < ans or (ans1 == ans and remainTime1 > remainTime):
                    ans = ans1
                    remainTime = remainTime1

        return ans,remainTime


    n = len(tasks)
    return dp((1<<n)-1)[0]


if __name__ == '__main__':
    print(minSessionsoptimized([1,2,3],3))
    print(minSessionsoptimized([3,1,3,1,1],8))