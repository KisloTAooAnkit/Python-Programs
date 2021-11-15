def nextPerm(string):
    arr = list(string)
    idx = -1
    n = len(arr)
    for i in range(n-1,0,-1):
        if arr[i] > arr[i-1]:
            idx = i-1
            break
    if idx == -1:
        return "no answer"
    swapPos = -1
    for i in range(idx+1,n):
        if arr[idx] < arr[i]:
            swapPos = i
    arr[idx],arr[swapPos] = arr[swapPos],arr[idx]
    start = idx+1
    end = n-1
    while(start<=end):
        arr[start],arr[end] = arr[end],arr[start]
        start+=1
        end-=1
    return "".join(arr)

s = "abdc"
print(nextPerm(s))
