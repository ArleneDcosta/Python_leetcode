import sys
from typing import List
from collections import defaultdict

'''Try making curr person with positive value as 0'''
def minTransfers(transactions: List[List[int]]) -> int:
    debts = defaultdict(int)
    for f,t,amount in transactions:
        debts[f] -= amount
        debts[t] += amount
    print(debts)
    debts_list = [debts[id] for id in debts if debts[id]]
    n = len(debts_list)
    print(debts_list)
    '''We assume that all debts from 0 -> (idx - 1) has aldready been settled
    We need to check that starting from idx any debt has not been settled'''
    def backtrack(idx):
        while idx < n and debts_list[idx] == 0:
            idx += 1
        if idx == n:
            return 0
        ans = sys.maxsize
        for i in range(idx + 1,n):
            '''There is no use setting or wasting a transaction on 0 so instead use value less than 0
            Also there is no point if one is 5 and another is 10 so use giving 5 to 10 we rather give to less than 0'''
            '''Below is greedy check'''
            if debts_list[idx] * debts_list[i] < 0:
                debts_list[i] += debts_list[idx]
                ans = min(ans,backtrack(idx + 1) + 1)
                '''Settle it back so that next might have clean slate'''
                debts_list[i] -= debts_list[idx]
        return ans


    return backtrack(0)






if __name__ == '__main__':
    print(minTransfers([[0,1,5],[2,0,5]]))