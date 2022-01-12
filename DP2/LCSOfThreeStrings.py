

def modifiedLCS(a,b,c,i,j,k,dp):
    
    if i>=len(a) or j>=len(b) or k>=len(c):
        return 0

    if dp[i][j][k] != -1:
        return dp[i][j][k]

    if a[i] == b[j] == c[k]:
        dp[i][j][k] = 1 + modifiedLCS(a,b,c,i+1,j+1,k+1,dp)
        return dp[i][j][k]

    ans = max(modifiedLCS(a,b,c,i,j,k+1,dp),modifiedLCS(a,b,c,i+1,j,k,dp),modifiedLCS(a,b,c,i,j+1,k,dp))
    dp[i][j][k] = ans
    return dp[i][j][k]


def LCSOfThree(a,b,c):
    
    dp = [[[-1 for _ in range(len(c)+1)] for _ in range(len(b)+1) ] for _ in range(len(a)+1)]
    return modifiedLCS(a,b,c,0,0,0,dp)


a = "geeks"
b = "geeksfor"
c = "geeksforgeeks"

print(LCSOfThree(a,b,c))