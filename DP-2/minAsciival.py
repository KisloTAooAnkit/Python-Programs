def minDelSum(s1,s2,m,n):
    if(m ==0 and n ==0):
        return 0
    
    if(m==0):
        ans=0
        for i in range(n):
            ans += ord(s2[i])
        return ans
    
    if(n==0):
        ans=0
        for i in range(m):
            ans += ord(s1[i])
        return ans
    
    if(s1[0]==s2[0]):
        return minDelSum(s1[1:],s2[1:],m-1,n-1)
    
    else:
        option1 = ord(s1[0]) + minDelSum(s1[1:],s2,m-1,n)
        option2 = ord(s2[0]) + minDelSum(s1,s2[1:],m,n-1)
        
        ans = min(option1,option2)
        return ans



    
def minDelSumDP(s1,s2,m,n,dp):
    if(m ==0 and n ==0):
        return 0
    
    if(m==0):
        ans=0
        for i in range(n):
            ans += ord(s2[i])
        return ans
    
    if(n==0):
        ans=0
        for i in range(m):
            ans += ord(s1[i])
        return ans
    
    if(dp[m][n]>-1):
        return dp[m][n]
    
    
    if(s1[0]==s2[0]):
        return minDelSumDP(s1[1:],s2[1:],m-1,n-1,dp)
    
    else:
        option1 = ord(s1[0]) + minDelSumDP(s1[1:],s2,m-1,n,dp)
        option2 = ord(s2[0]) + minDelSumDP(s1,s2[1:],m,n-1,dp)
        
        ans = min(option1,option2)
        dp[m][n] = ans
        return ans

a="nbzvshnmtlioe"
b="rudntqxfmslvpib"   


def dpCaller(a,b):
    m = len(a)
    n = len(b)
    dp =[[-1 for j in range(n+1)] for i in range(m+1)]
    return minDelSumDP(a,b,m,n,dp)    


print(dpCaller(a,b))

print(minDelSum(a,b,len(a),len(b)))        