

def helper(i,j,arr,dp,totalSum):

    if i == j:
        return arr[i]
    
    if dp[i][j] != -1:
        return dp[i][j]

    end = totalSum - helper(i,j-1,arr,dp,totalSum-arr[j])
    start = totalSum - helper(i+1,j,arr,dp,totalSum-arr[i])
    dp[i][j] = max(end,start)
    return max(end,start)



def optimalStrategyForGame(arr):
    n = len(arr)
    i = 0
    j = n-1
    dp = [[-1]*n for _ in range(n)]
    return helper(i,j,arr,dp,sum(arr))


a = [1,4,12,8]
print(optimalStrategyForGame(a))


#################################################  Optimal Strategy online solutions more intuitive 




def helper(i,j,arr,dp):
    if i>j:
        return 0

    if i == j:
        return arr[i]

    if dp[i][j] != -1:
        return dp[i][j]

    left = arr[i] + min(helper(i+2,j,arr,dp) , helper(i+1,j-1,arr,dp))
    right = arr[j] + min(helper(i,j-2,arr,dp), helper(i+1,j-1,arr,dp))

    dp[i][j] = max(left,right)
    return max(left,right)


def optimumStrat(arr):
    n = len(arr)
    dp = [[-1]*n for _ in range(n)]
    return helper(0,n-1,arr,dp)


a = [1,4,12,8]
print(optimumStrat(a))