def angryChildren(arr,k):
    arr.sort()
    n = len(arr)
    runningSum = 0
    diffOfWindow = 0
    for end in range(k):
        diffOfWindow += end*arr[end] - runningSum
        runningSum += arr[end]
    
    flag  = True
    start = 0
    ans = float("inf")
    while(end<n):
        if not flag:
            runningSum += arr[end]
            diffOfWindow += (end-start +1)*arr[end] - runningSum

        while(end-start+1 == k or flag):
            ans = min(diffOfWindow,ans)
            diffOfWindow -= runningSum - k*arr[start]
            runningSum -= arr[start]
            start +=1
            flag = False
        end +=1

    return ans
            
arr = [10,100,300,200,1000,20,30]
k = 3
print(angryChildren(arr,k))
