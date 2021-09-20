

#https://leetcode.com/problems/delete-operation-for-two-strings/

def helperDiff(s1,s2,m,n,dp):
    if(m == 0 or n ==0 ):
        return 0
    
    if(dp[m][n] > -1):
        return dp[m][n]
    
    ans = 0
    if(s1[0] == s2[0]):
        ans = 1 + helperDiff(s1[1:],s2[1:],m-1,n-1,dp)
        
    else:
        res1 = helperDiff(s1[1:],s2,m-1,n,dp)
        res2 = helperDiff(s1,s2[1:],m,n-1,dp)
        ans = max(res1,res2)
    dp[m][n] = ans
    return ans

def minDiff(s1,s2):
    m= len(s1)
    n= len(s2)
    dp =[[-1 for j in range(n+1)] for i in range(m+1)]
    val =  helperDiff(s1,s2,m,n,dp)
    return (m + n - 2*val)





a="leetcode"
b="0" 
print(minDiff(a,b))
    