import sys
def maxProfit(arr):
    profit = 0
    buyingPrice = sys.maxsize
    for i in range(0,len(arr)):
        if(buyingPrice>arr[i]):
            buyingPrice = arr[i]

        currentStockVal = arr[i]-buyingPrice
        if(profit<currentStockVal):
            profit = currentStockVal
        
    
    return profit


arr = [7,6,4,3,1]
print(maxProfit(arr))