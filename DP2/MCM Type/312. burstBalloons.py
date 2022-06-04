
def helper(arr,i,j,dp):
    if i > j:
        return 0

    if dp[i][j] != -1:
        return dp[i][j]
    
    ans = float("-inf")
    for k in range(i,j+1):
        left = helper(arr,i,k-1,dp)
        right = helper(arr,k+1,j,dp)
        
        prevBalloon = 1 if i == 0 else arr[i-1]
        nextBalloon = 1 if j+1 >= len(arr) else arr[j+1]

        currentBalloonPoints = prevBalloon * arr[k] * nextBalloon

        res = left + currentBalloonPoints + right
        ans = max(ans,res)
    dp[i][j] = ans 
    return ans





def maxCoins(arr):
    n = len(arr)
    dp = [[-1]*(n+1) for _ in range(n+1)]
    return helper(arr,0,n-1,dp)

arr = [3,1,5,8]
print(maxCoins(arr))