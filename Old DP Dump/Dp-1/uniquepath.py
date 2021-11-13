#https://leetcode.com/problems/unique-paths/

def UniquePath(currx,curry,endx,endy,dp):
    if(currx==endx and curry==endy):    
        return 1
    
    if(currx>endx or curry>endy ):
        return 0
    
    if(dp[currx][curry] != -1):
        return dp[currx][curry]
    
    ans=0
    ans += UniquePath(currx+1,curry,endx,endy,dp)
    ans += UniquePath(currx,curry+1,endx,endy,dp)
    
    dp[currx][curry] = ans
    
    return ans


def caller(m,n):
    dp = [ [-1 for j in range(n)] for i in range(m) ]
    
    return UniquePath(0,0,m-1,n-1,dp)
    
m,n = 3,7
print(caller(m,n))