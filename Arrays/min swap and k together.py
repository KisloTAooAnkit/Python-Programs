import sys
def minSwap (arr, n, k) : 
    candidates = 0 #windowsize
    for i in arr:
        if(i<=k):
            candidates+=1
    
    if(candidates<=0):
        return 0

    ans = sys.maxsize
    runningcand= 0
    start =0
    end = 0
    while(end<n):
        if(arr[end]<=k):
            runningcand +=1
        
        while(end-start+1 == candidates):
            ans = min(ans,end-start+1 - runningcand)
            if(arr[start]<=k):
                runningcand -=1
            start+=1
        end+=1

    return ans

arr = [4 ,16, 3 ,8 ,13 ,2 ,19 ,4, 12 ,2 ,7 ,17, 4, 19 ,1]
k = 9

print(minSwap(arr,len(arr),k))