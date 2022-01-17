def maximizeDist(arr):
    n = len(arr)
    temp = [n]*n
    lastOneIdx = -1
    
    for i in range(n):
        if arr[i] == 1:
            temp[i] = -1
            lastOneIdx = i
        if arr[i] == 0:
            if lastOneIdx == -1:
                continue
            else:
                temp[i] = abs(lastOneIdx-i)
    lastOneIdx = -1
    for i in range(n-1,-1,-1):
        if arr[i] == 1:
            lastOneIdx = i
        if arr[i] == 0:
            if lastOneIdx == -1:
                continue
            else:
                temp[i] = min(temp[i],abs(lastOneIdx-i))
    print(temp)
    return max(temp)