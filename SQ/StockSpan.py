def StockSpan(arr):
    n = len(arr)
    ans = [1]*n
    stack = []
    for i in range(n-1,-1,-1):
        while(stack and arr[stack[-1]]<arr[i]):
            idx = stack.pop()
            ans[idx] = abs(idx-i)
        stack.append(i)
    return ans

arr = [100,80,60,70,60,75,85]
print(StockSpan(arr))