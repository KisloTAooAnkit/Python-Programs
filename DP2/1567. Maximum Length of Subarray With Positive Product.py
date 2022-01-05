def maxLen(arr):
    n = len(arr)
    dp = [[0]*n for _ in range(2)]
    
    if arr[0] < 0:
        dp[0][0] = 0
        dp[1][0] = 1
    elif arr[0] > 0:
        dp[0][0] = 1
        dp[1][0] = 0
 
    ans = 0
    for i in range(1,n):
        val = arr[i]
        
        if val < 0 :
            dp[0][i] = 0 if dp[1][i-1] == 0 else dp[1][i-1] +1
            dp[1][i] = 1 if dp[0][i-1] == 0 else dp[0][i-1] +1

        if val > 0:
            dp[0][i] = 1 if dp[0][i-1] == 0 else dp[0][i-1] +1
            dp[1][i] = 0 if dp[1][i-1] == 0 else dp[1][i-1] +1

        ans = max(ans,dp[0][i])
    return ans

arr = [0,1,-2,-3,-4]
print(maxLen(arr))



############## O(1) Space Logic is same ############################
def getMaxLen(arr) -> int:
    n = len(arr)
    pp = 0
    pn = 0
    ans = 0
    if arr[0] < 0:
        pp = 0
        pn = 1
    elif arr[0] > 0:
        ans = 1
        pp = 1
        pn = 0

    
    for i in range(1,n):
        val = arr[i]
        cp,cn = 0,0
        if val < 0 :
            cp = 0 if pn == 0 else pn +1
            cn = 1 if pp == 0 else pp +1

        if val > 0:
            cp = 1 if pp == 0 else pp +1
            cn = 0 if pn == 0 else pn +1

        ans = max(ans,cp)
        pp,pn = cp,cn
    return ans