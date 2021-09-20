def nextPerm(arr):
    prev = float('-inf')
    possibleCandidate = 0
    n = len(arr)
    i = n-1
    while(i>=0):
        if arr[i] >= prev:
            prev = arr[i]
            
        else:
            break
        i-=1
    if i < 0:
        arr.sort()
        return

    val = arr[i]
    valIdx = i
    while(i+1<n):
        if arr[i+1] > val:
            possibleCandidate = i+1
        i+=1
    arr[valIdx],arr[possibleCandidate] = arr[possibleCandidate],arr[valIdx]
    i = valIdx +1
    j = n -1
    while(i<j):
        arr[i],arr[j] = arr[j],arr[i]
        i+=1
        j-=1

    return  
        

arr = [3,2,1]
#arr = [6,2,1,5,4,3,0]
print(nextPerm(arr))