
############################## RECURSIVE Brute Force #################################
def isPanlindrome(s,i,j):
    while(i<=j):
        if s[i] != s[j]:
            return False
        i+=1
        j-=1
    return True

def recursive(s,i,j):
    if i>j:
        return 0
    if i==j:
        return 1
    if s[i:j+1] == s[i:j+1:-1]:
        return 0
    res = float("inf")
    for k in range(i,j):
        ans = recursive(s,i,k) + recursive(s,k+1,j) + 1
        res = min(ans,res)
    return res
    
################################ DP ######################################

def dpRecursiveOne(s,i,j,dp,pal):
    if i>j:
        return 0
    if pal[i][j]:
        return 0
    if dp[i][j] != -1:
        return dp[i][j]
    
    res = float("inf")
    for k in range(i,j):
        ans = dpRecursiveOne(s,i,k,dp,pal) + dpRecursiveOne(s,k+1,j,dp,pal) + 1
        res = min(ans,res)
    dp[i][j] = res
    return res


############# Filling Palindrome Table ####################
def expand(s,start,end,dp,n):
    while(start>=0 and end <n and s[start] == s[end]):
        dp[start][end] = True
        start -=1
        end +=1
    
def fillPalindromeTable(s,isPalindrome,n):    
    for i in range(n):
        expand(s,i,i,isPalindrome,n)
        expand(s,i,i+1,isPalindrome,n)
###########################################################
    

################## DP Part -2 optitmized to get accepted on Leetcode #############

def dpRecursiveTwo(s,i,j,dp,pal):
    if i>j:
        return 0
    if pal[i][j]:
        return 0
    if dp[i][j] != -1:
        return dp[i][j]
    
    res = float("inf")
    for k in range(i,j):
        #### Optimization by skipping left calls if we have palindrome encountered ####
        if pal[i][k]:
            ans = dpRecursiveTwo(s,k+1,j,dp,pal) + 1
            res = min(ans,res)
    dp[i][j] = res
    return res




###################### Actual Call ########################
def minPalindromePartion(s):
    n = len(s)
    s = list(s)
    dp = [[-1]*(n+1) for _ in range(n+1)]
    pal = [[False]*(n) for _ in range(n)]
    fillPalindromeTable(s,pal,n)
    return dpRecursiveOne(s,0,n-1,dp,pal)

s = "nitin"
print(minPalindromePartion(s))    