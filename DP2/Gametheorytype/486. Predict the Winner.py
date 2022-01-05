class Solution:

    def helper(self,i,j,arr,dp,totalSum):

        if i == j:
            return arr[i]

        if dp[i][j] != -1:
            return dp[i][j]

        end = totalSum - self.helper(i,j-1,arr,dp,totalSum-arr[j])
        start = totalSum - self.helper(i+1,j,arr,dp,totalSum-arr[i])
        dp[i][j] = max(end,start)
        return max(end,start)
    
    
    
    def PredictTheWinner(self, arr) -> bool:
        n = len(arr)
        i = 0
        j = n-1
        dp = [[-1]*n for _ in range(n)]
        ans =  self.helper(i,j,arr,dp,sum(arr))
        return sum(arr) - ans <= ans