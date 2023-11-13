from typing import List

def minCost(s:str,cost:List[int]) -> int:
    n = len(s)
    ans = 0
    max_cost = 0
    for i in range(n):
        ans += cost[i]
        max_cost = max(max_cost,cost[i])
        print(i)
        if i == n - 1 or s[i] != s[i+1]:
            ans -= max_cost
            max_cost = 0

    return ans

if __name__ == '__main__':
    print(minCost("abaac",[1,2,3,4,5]))