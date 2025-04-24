from typing import List

def maxProfit(prices: List[int]) -> int:
    maxProfitarr = []
    maxelement = -100000
    for i in range(len(prices)-1,-1,-1):
        if prices[i] > maxelement:
            maxelement = prices[i]
        maxProfitarr.append(maxelement)

    maxProfitarr.reverse()

    maxProfit = -1000
    for i in range(len(prices)):
        currdiff = maxProfitarr[i] - prices[i]
        if currdiff > maxProfit:
            maxProfit = currdiff

    return maxProfit

if __name__ == '__main__':
    print(maxProfit([2,4,1]))
    print(maxProfit([7,1,5,3,6,4]))
    print(maxProfit([7,6,4,3,1]))