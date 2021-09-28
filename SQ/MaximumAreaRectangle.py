import sys
def largestRectangleArea(arr):
    n = len(arr) + 2
    ans = [0]*(n)
    arr = [-sys.maxsize] + arr + [-sys.maxsize]
    stack = []
    for i in range(n):
        while(stack and arr[stack[-1]]>arr[i]):
            idx = stack.pop()
            ans[idx] = abs(idx - i)
        stack.append(i)
    print(ans)
    stack = []
    for i in range(n-1,-1,-1):
        while(stack and arr[stack[-1]]>arr[i]):
            idx = stack.pop()
            ans[idx] += abs(idx - i)
        stack.append(i)

    res = 0
    for i in range(1,n-1):
        val = (ans[i] -1) * arr[i]
        if val >res:
            res = val
    return res

def maximalRectangle(matrix):
    if len(matrix) == 0:
        return 0
    ans = -sys.maxsize
    temp = [0]*len(matrix[0])
    for row in matrix:
        for idx,val in enumerate(row):
            if(val=='0'):
                temp[idx] = 0
            else:
                temp[idx] += int(row[idx])
        ans = max(ans,largestRectangleArea(temp))

    return ans

mat = [["1","0","1","0","0"],["1","0","1","1","1"],["1","1","1","1","1"],["1","0","0","1","0"]]
mat = [["0","1"],["1","0"]]
print(maximalRectangle(mat))