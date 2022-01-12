

def LCS(a,b,i,j,dp):

    if i >= len(a) or j >= len(a):
        return 0
    if dp[i][j] != -1:
        return dp[i][j]

    if a[i] == b[j] and i!=j:
        dp[i][j] = 1 + LCS(a,b,i+1,j+1,dp)
        return dp[i][j]
    

    ans1 = LCS(a,b,i,j+1,dp)
    ans2 = LCS(a,b,i+1,j,dp)

    dp[i][j] = max(ans1,ans2)

    return max(ans1,ans2)




def LRS(s):
    n = len(s)
    dp = [[-1 for _ in range(n+1)] for _ in range(n+1)]
    return LCS(s,s,0,0,dp)


s = "aab"
print(LRS(s))