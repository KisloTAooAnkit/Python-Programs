def buyMaxStocks(arr,amount):
    n = len(arr)
    arr = [(arr[i],i+1) for i in range(n)]
    
    arr.sort()
    totalStocksBought = 0
    for i in range(n):
        cost,quantity = arr[i][0],arr[i][1]
        maxStocksCanBeBought = amount//cost
        val = min(maxStocksCanBeBought,quantity)*cost
        amount -=val
        totalStocksBought += min(maxStocksCanBeBought,quantity)
    return totalStocksBought

arr = [10,7,19]
k = 45
print(buyMaxStocks(arr,k))