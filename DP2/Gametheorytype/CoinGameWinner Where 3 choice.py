

def helper(n,x,y,isATurnNow,dp):

    if n<0:
        if isATurnNow:
            return "A"
        else:
            return "B"
    if n ==0:
        if isATurnNow:
            return "B"
        else:
            return "A"
    if dp[n][isATurnNow] != -1:
        return dp[n][isATurnNow]

    ans1 = helper(n-1,x,y,not isATurnNow,dp)
    ansx = helper(n-x,x,y,not isATurnNow,dp)
    ansy = helper(n-y,x,y,not isATurnNow,dp)


    if isATurnNow:
        if (ans1 == "A" or ansx == "A" or ansy == "A"):
            dp[n][isATurnNow] = "A"
            return "A"
        else:
            dp[n][isATurnNow] = "B"
            return "B"

    
    if not isATurnNow: 
        if (ans1 == "B" or ansx == "B" or ansy == "B"):
            dp[n][isATurnNow] = "B"
            return "B"
        else:
            dp[n][isATurnNow] = "A"
            return "A"
    




def coinGame(n,x,y):
    dp = [[-1]*2 for _ in range(n+1)]
    return helper(n,x,y,True,dp)

def coinGameIterative(n,x,y):

    dp = [[0]*(n+1) for _ in range(2)]
    dp[0][0] = "B"
    dp[1][0] = "A"

    for i in range(1,n+1):
        
        if i>=1:
            dp[0][i] = dp[1][i-1] if dp[0][i] != "A" else "A"
            dp[1][i] = dp[0][i-1] if dp[1][i] != "B" else "B"
        if i>=x:
            dp[0][i] = dp[1][i-x] if dp[0][i] != "A" else "A"
            dp[1][i] = dp[0][i-x] if dp[1][i] != "B" else "B"
        if i>=y:
            dp[0][i] = dp[1][i-y] if dp[0][i] != "A" else "A"
            dp[1][i] = dp[0][i-y] if dp[1][i] != "B" else "B"
    return dp[0][n]


        




n = 10
x = 2
y = 4
print(coinGameIterative(n,x,y),coinGame(n,x,y))