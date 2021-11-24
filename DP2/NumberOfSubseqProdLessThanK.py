def helper(arr,n,idx,p,k):
    if n==0:
        if p<k :
            return 1
        else:
            return 0
    if p>=k:
        return 0
    ans1 = helper(arr,n-1,idx+1,p,k)
    ans2 = helper(arr,n-1,idx+1,p*arr[idx],k)
    return ans1 + ans2



def countSubseq(arr,k):
    ans = helper(arr,len(arr),0,1,k)
    return ans-1



def dpHelper(arr,n,idx,p,k,dp):
    if n==0:
        if p<k:
            return 1
        else:
            return 0
    if p>=k:
        return 0
    if dp[p][n] > -1:
        return dp[p][n]
    
    ans1 = dpHelper(arr,n-1,idx+1,p,k,dp)
    ans2 = dpHelper(arr,n-1,idx+1,p*arr[idx],k,dp)
    dp[p][n] = ans1 + ans2
    return dp[p][n]

def countSubseqDP(arr,k):
    n = len(arr)
    dp = [[-1 for _ in range(n+1)] for _ in range(k+1)]
    return dpHelper(arr,n,0,1,k,dp)-1

def countSubseqIterative(arr,k):
    n = len(arr)
    dp = [[-1 for _ in range(n+1)] for _ in range(k+1)]



arr = [1,2,3]
k = 4
print(countSubseqDP(arr,k))