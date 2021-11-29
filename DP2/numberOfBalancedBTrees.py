def countBBT(h):
    if h == 0:
        return 1
    if h == 1:
        return 1
    
    a = countBBT(h-1)*countBBT(h-1)
    b = countBBT(h-2)*countBBT(h-1)
    c = countBBT(h-1)*countBBT(h-2)
    return a + b + c

def countBBTDP(h,dp):
    if h ==0:
        return 1
    if h==1:
        return 1
    if dp[h] != -1:
        return dp[h]
    a = countBBTDP(h-1,dp)*countBBTDP(h-1,dp)
    b = countBBTDP(h-2,dp)*countBBTDP(h-1,dp)
    c = countBBTDP(h-1,dp)*countBBTDP(h-2,dp)
    dp[h] = a + 2*b 
    return dp[h]

h =3
def caller(h):
    dp = [-1]*(h+1)
    return countBBTDP(h,dp)

def countBBTIterative(h):
    dp = [1]*(h+1)
    for i in range(2,h+1):
        a = dp[i-1]*dp[i-1]
        b = dp[i-2]*dp[i-1]
        dp[i] = a + 2*b
    return dp[h]        

h = 3
print(countBBTIterative(h))
