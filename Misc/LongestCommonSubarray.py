

def Lcsub(a,b,m,n,dp,ans):
    if(m==0 or n==0):
        dp[m][n] = 0
        return 0

    if(dp[m][n]>-1):
        return dp[m][n]

    ans = 0
    if(a[0] == b[0]):
        dp[i][j] = 1+ Lcsub(a[1:],b[1:],m-1,n-1,dp,ans)
        

    Lcsub(a,b[1:],m,n-1,dp,ans)
    Lcsub(a[1:],b,m-1,n,dp,ans)

    dp[m][n]  ans
    return ans

def callDP(a,b):
    dp = [[-1 for j in range(len(b)+1)] for i in range(len(a)+1)]
    return Lcsub(a,b,len(a),len(b),dp,0)

a=[1,2,3,2,1]
b=[3,2,1,4,7]

print(callDP(a,b))
