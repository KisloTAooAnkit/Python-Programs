def jump(arr):
    n=len(arr)

    if(n<=1):
        return 0

    i=0
    jump = 0
    while(i<n-1):
        endpt = arr[i] + i if (arr[i]+i)<n-1 else n-1
        maxsum = 0
        maxidx = 0
        for j in range(i+1,endpt+1):
            val = arr[j] + j
            if(val>=maxsum):
                maxsum = val
                maxidx = j
        jump+=1
        i= maxidx

    return jump


arr = [2,3,1,1,4]
print(jump(arr))
