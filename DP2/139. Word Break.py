
def wordDict(s,i,j,dp,dic):
    if i>j:
        return False
    
    if dp[i][j] != None:
        return dp[i][j]
    
    if s[i:j+1] in dic:
        return True
    ans = False
    for k in range(i,j):
        left = wordDict(s,i,k,dp,dic)
        right = wordDict(s,k+1,j,dp,dic)
        ans = ans or (left and right)
        #early return beacuse if ans is true we dont want to process
        #it further aur agar false aarha hai toh ham aage explore karenge
        #khi aage true aajaye toh
        if ans:
            break
    dp[i][j] = ans
    return ans

def solve(s,wordic):
    n = len(s)
    dic = {i : 1 for i in wordic}
    dp = [[None]*(n+1) for _ in range(n+1)]
    return wordDict(s,0,n,dp,dic)



s = s = "catsandog"
dic =["cats","dog","sand","and","cat"]

print(solve(s,dic))