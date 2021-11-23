

def helper(n,x,y,z):
    if n<=0:
        return 0
    xcut = 0
    ycut = 0
    zcut = 0
    if n>=x:
        xcut = 1+helper(n-x,x,y,z)
    if n>=y:
        ycut = 1+helper(n-y,x,y,z)
    if n>=z:
        zcut = 1+helper(n-z,x,y,z)
    
    return max(xcut,ycut,zcut)

def maximizeCutSegments(n,x,y,z):
    return helper(n,x,y,z)

def maximizeCutSegIterative(n,x,y,z):
    dp = [0]*(n+1)
    for i in range(n+1):
        xcut = 0
        ycut = 0
        zcut = 0
        if x<=i and (dp[i-x]>0 or i-x ==0):
            xcut = dp[i-x] + 1
        if y<=i and (dp[i-y]>0 or i-y ==0):
            ycut = dp[i-y] + 1
        if z<=i and (dp[i-z]>0 or i-z ==0):
            zcut = dp[i-z] + 1
        dp[i] = max(xcut,ycut,zcut)

    return dp[n]

n = 7
x =5
y=5
z=2 
print(maximizeCutSegIterative(n,x,y,z))