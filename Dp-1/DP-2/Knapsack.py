
def knapsackHelper(val,wght,totalSpace,n):
    if(totalSpace <= 0):
        return 0
    
    if n==0:
        return 0
    
    option1 , option2 = 0,0
    currentpick = val[0]
    currentweight = wght[0]
    
    if(totalSpace>=currentweight):
        option1 = currentpick + knapsackHelper(val[1:],wght[1:],totalSpace-currentweight,n-1)
    
    option2 = knapsackHelper(val[1:],wght[1:],totalSpace,n-1)
    
    return max(option2,option1)
    

def knapsackHelperDP(val,wght,totalSpace,n,dp):
    
    if(totalSpace <= 0):
        return 0
    
    if n==0:
        return 0
    
    if dp[n][totalSpace] > -1:
        return dp[n][totalSpace]
    
    option1 , option2 = 0,0
    currentpick = val[0]
    currentweight = wght[0]
    if(totalSpace>=currentweight):
        option1 = currentpick + knapsackHelperDP(val[1:],wght[1:],totalSpace-currentweight,n-1,dp)
    
    option2 = knapsackHelperDP(val[1:],wght[1:],totalSpace,n-1,dp)
    
    ans = max(option2,option1)
    dp[n][totalSpace] = ans
    return ans
    

#not clear yet to be revised
def knapsack_IDP(arr,wght,totalspace,n,dp):
    
    for i in range(totalspace+1):
        dp[0][i] = 0
        
    for i in range(n+1):
        dp[i][0] = 0
        
    for i in range(1,n+1):
        for currentweight in range(1,totalspace+1):
            option1,option2 = 0,0
            option1 = dp[i-1][currentweight]
            if(wght[i-1]<=currentweight):
                option2 = arr[i-1] + dp[i-1][currentweight-wght[i-1]]
            
            dp[i][currentweight] = max(option1,option2)
            
    
    ans = dp[n][totalspace]
    return ans
        
    
    
    


def knapsack(arr,wght,totalw):
    dp = [[-1 for i in range(totalw+1)] for j in range(len(arr)+1)]
    return knapsack_IDP(arr,wght,totalw,len(arr),dp)


arr = [60,100,120]
w = [10,20,30]
maxw = 50

print(knapsack(arr,w,maxw))
    