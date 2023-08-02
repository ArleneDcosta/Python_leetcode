def maxProfit(prices):
    minprice = 100000
    maxprofit = 0;
    for i in range(0,len(prices)):
        if (prices[i] < minprice):
            minprice = prices[i];
        elif (prices[i] - minprice > maxprofit):
            maxprofit = prices[i] - minprice
        
    return maxprofit
    

print maxProfit([7,1,5,3,6,4])
print maxProfit([7,6,4,3,1] )
