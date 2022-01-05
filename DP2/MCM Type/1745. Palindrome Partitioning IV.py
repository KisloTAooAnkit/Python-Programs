

def helper(arr,count,i,j,dp,pal):
    
    if count <=0:
        return False
    
    if i ==j:
        return True
    
    if pal[i][j]:
        return True
    
    if dp[i][j] != None:
        return dp[i][j]
    
    ans = False
    for k in range(i,j):
        
        if pal[i][k]:
            ans = ans or helper(arr,count-1,k+1,j,dp,pal)
    dp[i][j] = ans
    return ans


def expand(s,start,end,dp,n):
    while(start>=0 and end <n and s[start] == s[end]):
        dp[start][end] = True
        start -=1
        end +=1
    
def fillPalindromeTable(s,isPalindrome,n):    
    for i in range(n):
        expand(s,i,i,isPalindrome,n)
        expand(s,i,i+1,isPalindrome,n)

def checkPartitioning(s):
    n = len(s)
    n = len(s)
    s = list(s)
    dp = [[None]*(n+1) for _ in range(n+1)]
    pal = [[False]*(n) for _ in range(n)]
    fillPalindromeTable(s,pal,n)
    return helper(s,2,0,n-1,dp,pal)

s = "acab"
print(checkPartitioning(s))