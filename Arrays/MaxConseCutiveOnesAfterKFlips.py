def longestOnes(arr,k):
    n= len(arr)
    start = 0
    end = 0
    ans = -1
    while(end<n):
        if arr[end] == 0:
            k-=1
        while(k<0):
            if arr[start] ==0:
                k+=1
            start +=1
        ans = max(ans,end-start+1)
        end +=1
    return ans