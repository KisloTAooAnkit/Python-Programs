
def sol(i,j,arr,flag,dp):
    if i > j:
        return 0
    
    if i == j:
        if flag == 1:
            return 1 if arr[i] == "T" else 0
        else:
            return 1 if arr[i] == "F" else 0

    if dp[i][j][flag] != -1:
        return dp[i][j][flag]
    
    falseCount = 0
    trueCount = 0
    for k in range(i+1,j,2):
        leftTrue = sol(i,k-1,arr,1,dp)
        rightTrue = sol(k+1,j,arr,1,dp)
        leftFalse = sol(i,k-1,arr,0,dp)
        rightFalse = sol(k+1,j,arr,0,dp)
        
        if arr[k] == "|":
            trueCount += (leftTrue * rightTrue) + (rightFalse * leftTrue) + (leftFalse * rightTrue)
            falseCount += (leftFalse*rightFalse)
        if arr[k] == "^":
            trueCount += (leftFalse * rightTrue) + (leftTrue*rightFalse)
            falseCount += (leftTrue * rightTrue) + (leftFalse*rightFalse)
        if arr[k] == "&":
            trueCount += (leftTrue*rightTrue)
            falseCount += (rightFalse * leftTrue) + (leftFalse * rightTrue)
            
    dp[i][j][flag] = trueCount if flag == 1 else falseCount
    return dp[i][j][flag]
        


def boolParenthe(expression):
    n = len(expression)
    dp = [[[-1 for _ in range(2)] for _ in range(n+1)] for _ in range(n+1)]
    return sol(0,n-1,expression,1,dp)


a ="T|T&F^T"
print(boolParenthe(a))