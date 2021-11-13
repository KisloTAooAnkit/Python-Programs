
#https://www.geeksforgeeks.org/count-subsequences-product-less-k/

def foo(arr,k,n,prod):
    if(n<0):
        return 0
    if(prod>k): #jabhi product ans ko cross karega wapas jao
        return 0
    ans =0
    res = prod * arr[n]
    if(res<k):
        ans += 1+foo(arr,k,n-1,res)
    ans += foo(arr,k,n-1,prod)

    return ans 


def fooDP(arr,k,n,prod,dp):
    if(n<0):
        return 0
    if(prod>k): #jabhi product ans ko cross karega wapas jao
        return 0
    
    if(dp[n][prod]>-1):
        return dp[n][prod]

    ans =0
    res = prod * arr[n]
    if(res<k):
        ans += 1+fooDP(arr,k,n-1,res,dp)
    ans += fooDP(arr,k,n-1,prod,dp)

    dp[n][prod] = ans 
    return ans 



def caller(arr,k):

    n= len(arr)
    dp = [[-1 for i in range(k)] for j in range(n) ]
    ans =  fooDP(arr,k,len(arr)-1,1,dp)
    return ans

nums = [1,2,3,4]
k = 10

print(caller(nums,k))
