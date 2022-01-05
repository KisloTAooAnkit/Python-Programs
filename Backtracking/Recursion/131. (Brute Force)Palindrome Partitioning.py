def expand(s,start,end,dp,n):
    while(start>=0 and end <n and s[start] == s[end]):
        dp[start][end] = True
        start -=1
        end +=1
    
def fillPalindromeTable(s,isPalindrome,n):    
    for i in range(n):
        expand(s,i,i,isPalindrome,n)
        expand(s,i,i+1,isPalindrome,n)

def helper(s,i,n,pal,res,temp):
    if i>=n:
        res.append(temp)
        return
    
    for k in range(i,n):
        if pal[i][k]:
            helper(s,k+1,n,pal,res,temp+[s[i:(k+1)]])
    return

def palindromicPartition(s):
    n = len(s)
    pal = [[False]*(n) for _ in range(n)]
    fillPalindromeTable(s,pal,n)
    res = []
    helper(s,0,n,pal,res,[])
    print(res)

s = "aab"
palindromicPartition(s)