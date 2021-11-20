def helper(word1,word2,m,n,s1,s2,k):
    if 0 == m or 0 == n:
        if k > 0:
            return float("-inf")
    if k == 0:
        return 0
    ans0 = float("-inf")
    if word1[s1] == word2[s2]:
        ans0 = ord(word1[s1]) + helper(word1,word2,m-1,n-1,s1+1,s2+1,k-1)
    
    ans1 = helper(word1,word2,m,n-1,s1,s2+1,k)
    ans2 = helper(word1,word2,m-1,n,s1+1,s2,k)
    
    return max(ans1,ans2,ans0)
            


def baalikaVadhu(word1,word2,k):
    m = len(word1)
    n = len(word2)
    ans = helper(word1,word2,m,n,0,0,k)
    if ans == float("-inf"):
        return 0
    return ans

#dp
def helper(word1,word2,m,n,s1,s2,k,dp):
    if 0 >= m or 0 >= n:
        if k > 0:
            return float("-inf")
        else:
            return 0
    if k == 0:
        return 0
    if dp[k][m][n] >-1:
        return dp[k][m][n]
    if word1[s1] == word2[s2]:
        ans0 = max( ord(word1[s1]) + 
            helper(word1,word2,m-1,n-1,s1+1,s2+1,k-1,dp),
            helper(word1,word2,m,n-1,s1,s2+1,k,dp),
            helper(word1,word2,m-1,n,s1+1,s2,k,dp)
            ) 
        dp[k][m][n] = ans0
        return ans0
    else:
        ans1 = helper(word1,word2,m,n-1,s1,s2+1,k,dp)
        ans2 = helper(word1,word2,m-1,n,s1+1,s2,k,dp)
        
        dp[k][m][n] = max(ans1,ans2)
        return dp[k][m][n]
            


def baalikaVadhuDp(word1,word2,k):
    m = len(word1)
    n = len(word2)
    dp = [[[-1 for _ in range(n+1)] for _ in range(m+1)] for _ in range(k+1)]
    ans = helper(word1,word2,m,n,0,0,k,dp)
    if ans == float("-inf"):
        return 0
    return ans

# a = "aaab"
# b = "bbcc"
# k = 1
# print(baalikaVadhuDp(a,b,k))

test = int(input())
for i in range(test):
    a = input()
    b = input()
    k = int(input())
    print(baalikaVadhuDp(a,b,k))