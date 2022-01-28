



def helper(n,aliceTurn,dp):
    
    if n==1:
        dp[n][aliceTurn] = True
        return True
    if n ==2:
        dp[n][aliceTurn] = False
        return False
    if dp[n][aliceTurn] != None:
        return dp[n][aliceTurn]
    ans = False
    start = int(n**(1/2)) + 1
    print(start)
    for i in range(start,-1,-1):
        val = i*i
        if val > n:
            continue
        if val == n:
            dp[n][aliceTurn] = True
            return True
        res = helper(n-val,1-aliceTurn,dp)
        ans = ans or not res
        if ans:
            dp[n][aliceTurn] = ans
            return True        
    dp[n][aliceTurn] = ans
    return ans

def solve(n):
    dp = [[None]*2 for _ in range(n+1)]
    return helper(n,1,dp)

n = 4
print(solve(n))