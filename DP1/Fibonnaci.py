def fibonacci(n,dp):
    if n == 0 or n == 1:
        return 1 
    
    if dp[n] > 0:
        return dp[n]
    
    ans = fibonacci(n-1,dp) + fibonacci(n-2,dp)
    dp[n] = ans
    return ans
def fibonacciIterativeDP(n):
    arr = [0]*100
    arr[0] = 1
    arr[1] = 1
    for i in range(2,n+1):
        arr[i] = arr[i-1] + arr[i-2]
    output = arr[n]
    del arr
    return output

dp = [0]*100
print(fibonacci(5,dp))
print(fibonacciIterativeDP(5))