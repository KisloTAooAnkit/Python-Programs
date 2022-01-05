

def helper(arr,idx,n,isBought,k,dp):

    if n == 0 or n == 1:
        return 0
    if k == 0:
        return 0

    if dp[n][isBought][k] != -1:
        return dp[n][isBought][k]

    if not isBought:
        buy = helper(arr,idx+1,n-1,1,k,dp) - arr[idx]
        skip = helper(arr,idx+1,n-1,isBought,k,dp)
        dp[n][isBought][k] = max(skip,buy)
        return dp[n][isBought][k]
    else:
        sell = arr[idx] + helper(arr,idx+1,n-1,0,k-1,dp)
        hold = helper(arr,idx+1,n-1,isBought,k,dp)
        dp[n][isBought][k] = max(hold,sell)
        return dp[n][isBought][k]

    

def bestTimeToSell(arr):
    n = len(arr)
    dp = [[[-1 for _ in range(3)] for _ in range(2)] for _ in range(n+1)]
    return helper(arr,0,n,0,2,dp)



prices =[2,1,4,5,2,9,7]

print(bestTimeToSell(prices))