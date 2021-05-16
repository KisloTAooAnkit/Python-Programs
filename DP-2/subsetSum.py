#recursive solution is pending



def subsetSum(val,sum):
    n= len(val)
    dp = [[False for i in range(sum+1)] for j in range(n+1)]
    
    for i in range(sum+1):
        dp[0][i] = False
    
    for j in range(n+1):
        dp[j][0] = True
        
    for i in range(1,n+1):
        for j in range(1,sum+1):
            ans2 =0
            ans1 = dp[i-1][j]
            pickednumber = val[i-1]
            if(j-pickednumber>=0):
                ans2 = dp[i-1][j-pickednumber]
            
            dp[i][j] = ans1 or ans2
    
    return dp[n][sum] 

#iska explanation = https://docs.google.com/document/d/1PP0EO-pTgcETNAw8AL_dc-zIrxsANzU4clvgrkDA4pQ/edit
def subsetSumSpaceOpt(val,sum):
    n= len(val)
    dp = [[False for i in range(sum+1)] for j in range(2)]
    
    for i in range(sum+1):
        dp[0][i] = False
    
    for j in range(2):
        dp[j][0] = True
        
    flag = 1
        
    for i in range(1,n+1):
        for j in range(1,sum+1):
            ans2 =0
            ans1 = dp[flag^1][j]
            pickednumber = val[i-1]
            if(j-pickednumber>=0):
                ans2 = dp[flag^1][j-pickednumber]
            dp[flag][j] = ans1 or ans2
        flag = flag ^ 1
    
    
    return dp[flag^1][sum] 






val = [1,3,5,7,9]
sum = 12

print(subsetSumSpaceOpt(val,sum))