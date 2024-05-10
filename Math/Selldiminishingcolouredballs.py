from typing import List

def maxProfit(inv: List[int], orders: int) -> int:
    def getSum(start,end):
        return start * (start + 1)//2 - end * (end + 1) // 2
    inv.sort(reverse=True)
    factor = 1 # how many colours have the same amount
    n = len(inv)
    i = 0
    ans = 0
    while(orders > 0):
        #if we can make sales for all factors
        if i < n-1 and inv[i] > inv[i+1] and orders >= factor * (inv[i] - inv[i+1]):
            ans += factor * getSum(inv[i],inv[i+1])
            orders -= factor * (inv[i] - inv[i+1])

        # if we cannot make sales for all factors since last obj in inventory or no of orders are less than all inv objects
        elif i == n-1 or inv[i] > inv[i+1]:
            sell_all_times = orders // factor
            ans += factor * getSum(inv[i],inv[i] - sell_all_times)
            remain_orders = orders % factor
            ans += remain_orders * (inv[i] - sell_all_times)
            break

        # if inv[i] == inv[i+1]
        factor +=1
        i+=1
    return ans % (10**9+7)

if __name__ == '__main__':
    print(maxProfit(inv = [2,5], orders = 4))
    print(maxProfit(inv = [3,5], orders = 6))
    print(maxProfit(inv = [2,8,4,10,6], orders = 20))

'''
LOGIC:
a)
8 6 6 and orders = 18
ans += 1 * getSum(8,6)
8 + 7 
inventory = 6 6 6 
orders -= factor * (inv[i] - inv[i+1])
b)
6 6 6 and orders = 16
so
sell_all_times = 16 // 3 = 5
 ans += 3 * getSum(6,1)
 inventory = 
 6 6 6
 5 5 5
 4 4 4
 3 3 3
 2 2 2
 1
remain_orders = 16 % 3 = 1
ans += 1 * (6 - 5)
this is the logic for the second part

'''