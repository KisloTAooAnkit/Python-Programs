<<<<<<< Updated upstream



def solve(arr):
    n = len(arr)
    zero = [0]*(n+1)
    ones = [0]*(n+1)
    prevZeroCount = 0
    for i in range(n+1):
        zero[i] = prevZeroCount
        if i < n and arr[i] == 0:
            prevZeroCount +=1
    oc = 0
    for i in range(n-1,-1,-1):
        if arr[i] == 1:
            oc+=1
        ones[i] = oc

    ans = []
    for i in range(0,n+1):
        prev = zero[i]
        nxt = ones[i]
        ans.append((prev+nxt,i))
    ans.sort(key=lambda x :x[0])
    maxVal = -1
    res = []
    while ans:
        if ans[-1][0] >= maxVal:
            res.append(ans[-1][1])
            maxVal = ans[-1][0]
        ans.pop()
    
<<<<<<< Updated upstream
    if n==1:
        dp[n][aliceTurn] = True
        return True
    if n ==2:
        dp[n][aliceTurn] = False
        return False
    if dp[n][aliceTurn] != None:
        return dp[n][aliceTurn]
    ans = False
    start = int(n**(1/2)) + 1
    print(start)
    for i in range(start,-1,-1):
        val = i*i
        if val > n:
            continue
        if val == n:
            dp[n][aliceTurn] = True
            return True
        res = helper(n-val,1-aliceTurn,dp)
        ans = ans or not res
        if ans:
            dp[n][aliceTurn] = ans
            return True        
    dp[n][aliceTurn] = ans
    return ans

def solve(n):
    dp = [[None]*2 for _ in range(n+1)]
    return helper(n,1,dp)

n = 4
print(solve(n))
=======
>>>>>>> Stashed changes
=======
    return res    
    
arr =[1]
print(solve(arr))
>>>>>>> Stashed changes
