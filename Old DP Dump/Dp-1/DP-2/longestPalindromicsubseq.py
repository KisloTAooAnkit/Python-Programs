
#plain recursive
def caller(s1,s2,m,n):
    if(m < 0 or n < 0):
        return 0

    ans = 0

    if(s1[m] == s2[n]):
        ans = 1+caller(s1,s2,m-1,n-1)
        return ans

    option1 = caller(s1,s2,m-1,n)
    option2 = caller(s1,s2,m,n-1)

    ans = max(option1,option2)
    return ans

#recursive dp 0(n^2)
def callerDP(s1,s2,m,n,dp):
    if(m < 0 or n < 0):
        return 0


    if(dp[m][n]>-1):
        return dp[m][n]
    ans = 0

    if(s1[m] == s2[n]):
        ans = 1+callerDP(s1,s2,m-1,n-1,dp)
        return ans

    option1 = callerDP(s1,s2,m-1,n,dp)
    option2 = callerDP(s1,s2,m,n-1,dp)

    ans = max(option1,option2)
    dp[m][n] = ans
    return ans

#iterative dp O(n^2)
def callerDP_I(s1,s2):
    m= len(s1)
    dp = [[0 for i in range(m+1)] for j in range(m+1)]
    # dp[0][0] = 0
    # dp[1][0] = 1
    # dp[0][1] = 1

    for i in range(1,m+1):
        for j in range(1,m+1):
            if(s1[m-i] == s2 [m-j]):
                dp[i][j] = 1 + dp [i-1][j-1]
            else:
                dp[i][j] = max(dp[i-1][j],dp[i][j-1])
    
    return dp[m][m] 

#iterative dp with SC O(2n)
def callerDP_I_Optimized(s1,s2):
    m= len(s1)
    dp = [[0 for i in range(m+1)] for j in range(2)]

    flag = 1

    for i in range(1,m+1):
        for j in range(1,m+1):
            if(s1[m-i] == s2[m-j]):
                dp[flag][j] = 1 + dp[flag^1][j-1]
            else:
                dp[flag][j] = max(dp[flag^1][j],dp[flag][j-1])
        flag = flag^1
    
    return dp[flag^1][m]


def longestPalindromeSubseq(s):
    s2 = s[::-1]
    m= len(s)
    dp = [[-1 for i in range(m+1)] for j in range(m+1)]
    #return callerDP(s,s2,m-1,m-1,dp)
    return callerDP_I_Optimized(s,s2)


s = "cbba"

print(longestPalindromeSubseq(s))