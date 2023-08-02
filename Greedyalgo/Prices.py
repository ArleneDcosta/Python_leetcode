def solve(prices):
    minelement = prices[0]
    maxelement = prices[0]
    profit = maxelement - minelement
    for i in range(1,len(prices)):
        if prices[i] < maxelement:
            profit += (maxelement - minelement)
            minelement = prices[i]
            maxelement = prices[i]
        else:
            maxelement = prices[i]
    
    if prices[len(prices)-1] >= maxelement and (maxelement != minelement):
        profit += maxelement - minelement
    return(profit)      
        
print(solve([7,1,5,3,6,4]))
print(solve([1,2,3,4,5]))
print(solve([7,6,4,3,1]))
print(solve([6,1,3,2,4,7]))
