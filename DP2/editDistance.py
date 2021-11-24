

def editDistance(word1,word2):
    if len(word1) == 0 or len(word2) == 0:
        return max(len(word1),len(word2))
    
    if word1[0] == word2[0]:
        return editDistance(word1[1:],word2[1:])
    
    ins = 1+editDistance(word2[0]+word1,word2)
    
    rem = 1+editDistance(word1[1:],word2)
    
    new = word1[:]
    new[0] = word2[0]
    
    rep = 1+editDistance(new,word2)
    
    return min(ins,rep,rem)

def dphelper(word1,word2,m,n,s1,s2,dp):
    if m == 0 or n== 0:
        return max(m,n)

    if dp[m][n] > -1:
        return dp[m][n]
    
    if word1[s1] == word2[s2]:
        dp[m][n] = dphelper(word1,word2,m-1,n-1,s1+1,s2+1,dp)
        return dp[m][n]
    else:
        #rem
        removeOperation = 1 + dphelper(word1,word2,m-1,n,s1+1,s2,dp)
        #repl
        replaceOperation = 1 + dphelper(word1,word2,m-1,n-1,s1+1,s2+1,dp)
        #ins
        insertOperation = 1 + dphelper(word1,word2,m,n-1,s1,s2+1,dp)
        
        dp[m][n] = min(insertOperation,removeOperation,replaceOperation)
        return dp[m][n]

def editDistanceDpRecursive(word1,word2):
    l1 = list(word1)
    l2 = list(word2)
    m = len(word1)
    n = len(word2)
    dp = [[-1]*(n+1) for _ in range(m+1)]
    ans = dphelper(l1,l2,m,n,0,0,dp)
    return ans

def editDistIterative(word1,word2):
    m = len(word1)
    n = len(word2)
    dp = [[0]*(n+1) for _ in range(m+1)]
    
    for i in range(m+1):
        dp[i][0] = i
        
    for j in range(n+1):
        dp[0][j] = j        

    for i in range(1,m+1):
        for j in range(1,n+1):
            if word1[m-i] == word2[n-j]:
                dp[i][j] = dp[i-1][j-1]
            else:
                ins = 1+dp[i][j-1]
                rep = 1+dp[i-1][j-1]
                rem = 1+dp[i-1][j]
                dp[i][j] = min(ins,rep,rem)
    print(dp)
    return dp[m][n]


a = "horse"
b = "ros"
print(editDistIterative(a,b))