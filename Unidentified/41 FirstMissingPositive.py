def solve(arr):
    onePresent = False
    n = len(arr)
    for i in range(n):
        if not 1 <= arr[i] <= n:
            arr[i] = 1
        elif arr[i] == 1:
            onePresent = True
    
    if not onePresent:
        return 1
    
    for i in range(n):        
        idx = abs(arr[i]) - 1
        arr[idx] = - abs(arr[idx])

    for i in range(n):
        if arr[i] > 0:
            return i+1
    
    return n+1

nums = [7,8,9,11,12]
print(solve(nums))