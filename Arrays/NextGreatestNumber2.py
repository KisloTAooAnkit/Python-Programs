def nextGreaterElement(n):
    arr = [int(x) for x in str(n)]
    n = len(arr)
    startingDigit = arr[0]
    arr.sort()
    if startingDigit==arr[-1]:
        return -1
    nextGreaterval = 0
    nextGreatervalIdx = 0
    for i in range(n):
        if arr[i] >startingDigit:
            nextGreaterval = arr[i]
            nextGreatervalIdx = i
            break   

    for i in range(n):
        if i == nextGreatervalIdx:
            continue
        nextGreaterval = nextGreaterval*10 + arr[i]
    
    if nextGreaterval > 2**31 -1:
        return -1
    return nextGreaterval

n = 41414722
print(nextGreaterElement(n))

