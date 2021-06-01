def minDistance(s1,s2,m,n,dp):
    if m ==0:
        return n
    if n == 0:
        return m
    
    
    if dp[m][n] != -1:
        return dp[m][n]
    
    if(s1[0]==s2[0]):
        return minDistance(s1[1:],s2[1:],m-1,n-1,dp)
    
    ans = 0
    ##insert
    temp = s2[0] + s1
    option1 = 1 + minDistance(temp,s2,m+1,n,dp)
    ##delete
    temp = s1[1:]
    option2 = 1 + minDistance(temp,s2,m-1,n,dp)
    ##replace
    temp = s2[0] + s1[1:]
    option3 = 1 + minDistance(temp,s2,m,n,dp)
    
    ans = min(option1,option2,option3)
    
    dp[m][n] = ans
    return ans
    
    
def callerDp(s1,s2):
    m= len(s1)
    n = len(s2)
    
    dp = [[-1 for j in range(n+1)] for i in range (m+n+1)]
    
    return minDistance(s1,s2,m,n,dp)
    
    
a = "aaaaaazzzzzzz"
b = "zzzzzaaaaaaa"

print(callerDp(a,b))