def longestCommonSubstring(s1,s2):
    n1 = len(s1)
    n2 = len(s2)
    
    dp = [[0]*(n2+1) for _ in range(n1+1)]
    ans = 0
    for i in range(1,n1+1):
        for j in range(1,n2+1):
            if s1[n1-i] == s2[n2-j]:
                dp[i][j] = 1 + dp[i-1][j-1]
                ans = max(ans,dp[i][j])
            else:
                dp[i][j] = 0
    return ans


a = "12321"
b = "32147"
print(longestCommonSubstring(b,a))
    