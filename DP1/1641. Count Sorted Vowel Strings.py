def dfs(n,k,dp):
    if n==0:
        return 0
    if n==1:
        return k
    if (n,k) in dp:
        return dp[(n,k)]
    ans = 0
    for i in range(0,k):
        ans += dfs(n-1,k-i,dp)
    dp[(n,k)] = ans
    return ans
        


def countVowelStr(n):
    k = 5
    dp = dict()
    return dfs(n,k,dp)

n = 33
print(countVowelStr(n))