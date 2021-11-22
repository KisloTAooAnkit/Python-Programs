def helper(arr,isBought,k,ans):
    if len(arr) == 0:
        return 0 
    if k == 0:
        return 0
    if not isBought:
        immediateAction = helper(arr[1:],True,k,ans) - arr[0]
        hold = helper(arr[1:],isBought,k,ans)
        return max(hold,immediateAction)
    else:
        immediateAction = arr[0] + helper(arr[1:],False,k-1,ans)
        hold = helper(arr[1:],isBought,k,ans)
        return max(hold,immediateAction)
    
    


def traderProfit(k,arr):
    ans = [0]
 
    return helper(arr,False,k,ans)


def helperDP(arr,isBought,k,dp,n,idx):
    if n <= 0:
        return 0 
    if k == 0:
        return 0
    if dp[isBought][n][k] > -1:
        return dp[isBought][n][k]
    ans = 0
    if isBought == 0:
        immediateAction = helperDP(arr,1,k,dp,n-1,idx+1) - arr[idx]
        hold = helperDP(arr,isBought,k,dp,n-1,idx+1)
        ans = max(hold,immediateAction)
        
    else:
        immediateAction = arr[idx] + helperDP(arr,0,k-1,dp,n-1,idx+1)
        hold = helperDP(arr,isBought,k,dp,n-1,idx+1)
        ans = max(hold,immediateAction)
    
    dp[isBought][n][k] = ans
    return dp[isBought][n][k]


def traderProfitDP(arr,k):
    n = len(arr)
    dp = [[[-1]*(k+1) for _ in range(n+1)] for _ in range(2)]
    return helperDP(arr,0,k,dp,n,0)

arr = [3,2,6,5,0,3]
k =2

print(traderProfitDP(arr,k),traderProfit(k,arr))