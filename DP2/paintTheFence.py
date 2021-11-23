def helper(n,k,flag):



    if n == 0:
        return 1

    if k ==0:
        return 0
        
    if flag ==2:
        ans= helper(n-1,k-1,0)
        return k*ans
    else:
        ans1 = helper(n-1,k,flag+1)
        ans2 = helper(n-1,k-1,0)
        return k + ans1 + k*ans2



def paintTheFence(n,k):
    return helper(n,k,0)

n = 3
k = 2
print(paintTheFence(n,k))