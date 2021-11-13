def alphaCodes(n):
    if n == 0:
        return 0
    if n < 11:
        return 1
    
    
    ans2 = 0
    ans1 = alphaCodes(n//10)
    doubleDigit = n%100
    if doubleDigit <= 26:
        ans2 = alphaCodes(n//100)
    return ans1 + ans2

def alphaCodesDP(n,dp):
    if n == 0:
        return 1
    if n < 11:
        return 1
    if n in dp:
        return dp[n]
    ans2 = 0
    ans1 = 0
    singleDigit = n%10
    if singleDigit>0:
        ans1 = alphaCodesDP(n//10,dp)
    doubleDigit = n%100
    if doubleDigit <= 26:
        ans2 = alphaCodesDP(n//100,dp)
    dp[n] = ans2 + ans1
    return dp[n]

def alphaCodesDpIterative(n):
    inputArr = []
    while(n>0):
        inputArr.append(n%10)
        n//=10
    inputArr = inputArr[::-1]
    dp = [0] * (len(inputArr)+1)
    dp[0] = 1
    dp[1] = 1
    for i in range(2,len(inputArr)+1):
        dp[i] = dp[i-1]
        if inputArr[i-2]*10 + inputArr[i-1] <=26:
            dp[i] += dp[i-2]
    return dp[len(inputArr)]
    
n = 25113
dp = dict()
print(alphaCodesDP(n,dp))
print(alphaCodesDpIterative(n))

