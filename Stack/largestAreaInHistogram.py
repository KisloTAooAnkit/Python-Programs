import sys
def largestRectangleArea(arr):
    n = len(arr) + 2
    ans = [0]*(n)
    arr = [-sys.maxsize] + arr + [-sys.maxsize]
    stack = []
    for i in range(n):
        while(stack and arr[stack[-1]]>=arr[i]):
            idx = stack.pop()
            ans[idx] = abs(idx - i)
        stack.append(i)
    print(ans)
    stack = []
    for i in range(n-1,-1,-1):
        while(stack and arr[stack[-1]]>=arr[i]):
            idx = stack.pop()
            ans[idx] += abs(idx - i)
        stack.append(i)
    print(ans)

    res = 0
    for i in range(1,n-1):
        val = (ans[i] -1) * arr[i]
        if val >res:
            res = val
    return res




a = [6,1,3]
print(largestRectangleArea(a))