import sys
def maxProfit(arr):
    totalProfit = 0
    profit = 0
    buyingPrice = sys.maxsize
    loss_val = -sys.maxsize
    arr.append(loss_val)
    for i in range(0,len(arr)):
        val = arr[i]
        if(buyingPrice>val):
            buyingPrice = val


        currentStockVal = val-buyingPrice
        if(profit<currentStockVal):
            profit = currentStockVal
        
        elif(currentStockVal<profit):
            totalProfit += profit
            profit = 0
            buyingPrice = val
        
        
    
    return totalProfit


arr = [1,2,3,4,5]
print(maxProfit(arr))