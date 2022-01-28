def maxSum(arr,n):
    arr.sort()

    l = 0
    r = n-1
    ans = 0
    while(l<r):
        ans += arr[l]
        ans -= arr[r]
        l+=1
        r-=1
    return ans * 2
