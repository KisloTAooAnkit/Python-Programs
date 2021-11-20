def longestComSubseq(s1,s2):
    if len(s1) == 0 or len(s2) == 0:
        return 0
    
    if s1[0] == s2[0]:
        return 1 + longestComSubseq(s1[1:],s2[1:])
    
    ans1 = longestComSubseq(s1,s2[1:])
    ans2 = longestComSubseq(s1[1:],s2)
    return max(ans2,ans1)
#recursive dp
def helper(s1,s2,start1,start2,len1,len2,dp):
    if len1 == 0 or len2 ==0:
        return 0
    if dp[len1][len2] > -1:
        return dp[len1][len2]
    
    if s1[start1] == s2[start2]:
        dp[len1][len2] = 1 + helper(s1,s2,start1+1,start2+1,len1-1,len2-1,dp)
        return dp[len1][len2]
    
    ans1 = helper(s1,s2,start1,start2+1,len1,len2-1,dp)
    ans2 = helper(s1,s2,start1+1,start2,len1-1,len2,dp)
    dp[len1][len2] = max(ans1,ans2)
    return dp[len1][len2]

def lcsDP(s1,s2):
    n = len(s1)
    m = len(s2)
    dp = [[-1 for _ in range(m+1)] for _ in range(n+1)]
    ans = helper(s1,s2,0,0,n,m,dp)
    return ans


def lcsIterative(s1,s2):
    n = len(s1)
    m = len(s2)
    dp = [[0 for _ in range(m+1)] for _ in range(n+1)]
    for i in range(1,n+1):
        for j in range(1,m+1):
            if s1[n-i] == s2[m-j]:
                dp[i][j] = 1+ dp[i-1][j-1]
            else:
                dp[i][j] = max(dp[i][j-1],dp[i-1][j])
    return dp[n][m]  

a = "abcdef"
b = "def"
print(lcsIterative(a,b))