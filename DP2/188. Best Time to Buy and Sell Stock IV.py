
def maxProfit(k,prices):
    ans = 0
    buyingPrice = prices[0]
    previousProfit = 0
    n = len(prices)
    i = 1
    while(i<n):
        curval = prices[i]
        if curval > prices[i-1]:
            previousProfit = curval - buyingPrice
        elif curval < prices[i-1] and k>0:
            ans += previousProfit
            buyingPrice = curval
            previousProfit = 0
            k-=1
        i+=1
    return ans + previousProfit 
        
        
        