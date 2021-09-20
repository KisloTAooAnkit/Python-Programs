def NGR(arr):
    stack = []
    n = len(arr)
    for i in range(0,n):
        while(stack and arr[stack[-1]]<arr[i]):
            idx = stack.pop(-1)
            arr[idx] = arr[i]
        stack.append(i)
        arr[i] = 0
    return arr


arr = [1,2,3,4,5,6,7]
print(NGR(arr))
