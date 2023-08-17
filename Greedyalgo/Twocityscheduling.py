from typing import List
from heapq import heapify
from collections import defaultdict

def twoCitySchedCost(costs: List[List[int]]) -> int:
    costs.sort(key = lambda x: abs(x[0] - x[1]),reverse= True)
    print(costs)
    ans = 0
    Acount = Bcount = 0
    n = len(costs) // 2
    for Acost,Bcost in costs:
        if (Acost < Bcost and Acount < n) or Bcount == n:
            ans += Acost
            Acount += 1
        #For cases like [10,10],[20,20],[400,400],[60,60]
        elif Acost >= Bcost or Acount == n:
            ans += Bcost
            Bcount += 1
    #print(costs)
    return ans
if __name__ == '__main__':
    # print(twoCitySchedCost([[259,770],[448,54],[926,667],[184,139],[840,118],[577,469]]))
    # print(twoCitySchedCost([[10,20],[30,200],[400,50],[30,20]]))
    print(twoCitySchedCost([[40,30],[50,40],[400,390],[50,20]]))
    print(twoCitySchedCost([[400, 390], [50, 20],[40, 30], [50, 40]]))