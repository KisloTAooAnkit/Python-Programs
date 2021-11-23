def helper(arr,i,n,k,dic):
    
    if n - i ==1:
        return True
    if n - i < 1:
        return False

    ans1 = False
    ans2 = False
    ans3 = False
    if k-1 >0:
        newStone = arr[i] + k-1
        if newStone in dic:
            nextIdx = dic[newStone]
            ans1 = helper(arr,nextIdx,n,k-1,dic)
    if k>0:
        newStone = arr[i] + k
        if newStone in dic:
            nextIdx = dic[newStone]
            ans2 = helper(arr,nextIdx,n,k,dic)
    
    #k+1
    newStone = arr[i] + k+1
    if newStone in dic:
        nextIdx = dic[newStone]
        ans3 = helper(arr,nextIdx,n,k+1,dic)
    
    return ans1 or ans2 or ans3

def canCross(stones):
    dic = dict()
    n = len(stones)
    for i in range(n):
        dic[stones[i]] = i
    return helper(stones,0,n,0,dic)
    

def helperDP(arr,i,n,k,dic,dp):
    if n-i == 1:
        return True
    if n-i < 0 :
        return False
    
    if dp[n-i][k] != -1:
        return dp[n-i][k] == 1
    
    ans1 = False
    ans2 = False
    ans3 = False
    if k-1 >0:
        newStone = arr[i] + k-1
        if newStone in dic:
            nextIdx = dic[newStone]
            ans1 = helperDP(arr,nextIdx,n,k-1,dic,dp)
    if k>0:
        newStone = arr[i] + k
        if newStone in dic:
            nextIdx = dic[newStone]
            ans2 = helperDP(arr,nextIdx,n,k,dic,dp)
    
    #k+1
    newStone = arr[i] + k+1
    if newStone in dic:
        nextIdx = dic[newStone]
        ans3 = helperDP(arr,nextIdx,n,k+1,dic,dp)
    
    dp[n-i][k] = 1 if ans1 or ans2 or ans3 else 0
    return dp[n-i][k]

def canCrossDP(stones):
    dic = dict()
    n = len(stones)
    for i in range(n):
        dic[stones[i]] = i
    dp = [[-1]*(n+1) for _ in range(n+1)]
    return helperDP(stones,0,n,0,dic,dp) == 1

def canCrossIterative(stones):
    dic = dict()
    n = len(stones)
    for i in range(n):
        dic[stones[i]] = i
    dp = [[False]*(n+1) for _ in range(n+1)]
    
    for i in range(n+1):
        dp[i][1] = True
    
    for k in range(1,n):
        for i in range(2,n+1):
            ans1,ans2,ans3 = False,False,False
            if k-1>0:
                newStone = stones[n-i] + k-1
                if newStone in dic:
                    nextIdx = dic[newStone]
                    ans1 = dp[k-1][n-nextIdx]
            if k>0:
                newStone = stones[n-i] + k
                if newStone in dic:
                    nextIdx = dic[newStone]
                    ans2 = dp[k][n-nextIdx]
            if k+1>0 and k:
                newStone = stones[n-i] + k+1
                if newStone in dic:
                    nextIdx = dic[newStone]
                    ans3 = dp[k+1][n-nextIdx]
            dp[k][i] = ans1 or ans2 or ans3 
    
    for i in range(n+1):
        if dp[i][n]:
            return True
    return False

    

stones = [0,1,2,3,4,8]
print(canCrossIterative(stones))