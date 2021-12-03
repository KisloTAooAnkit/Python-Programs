def calcMaxArea(arr,n):
    ans = 0
    #NSR
    stack = []
    temp = [0]*n
    for i in range(n):
        while(stack and arr[stack[-1]]>arr[i]):
            idx = stack.pop()
            temp[idx] = abs(i-idx)
        stack.append(i)
    while stack:
        idx = stack.pop()
        temp[idx] = n-idx

    #NSL
    for i in range(n-1,-1,-1):
        while(stack and arr[stack[-1]]>arr[i]):
            idx = stack.pop()
            temp[idx] += abs(i-idx) -1
        stack.append(i)
    
    while stack:
        idx = stack.pop()
        temp[idx] += abs(0-idx)
    
    for i in range(n):
        ans = max(
            ans,
            temp[i]*arr[i]
        )
    return ans

def maximalRect(grid):
    n = len(grid)
    
    rows = len(grid)
    cols = len(grid[0])
    temp = [0]*cols
    ans = 0
    for i in range(0,rows):
        for col in range(cols):
            if grid[i][col] == "0":
                temp[col] = 0
            else:
                temp[col] +=1

        ans = max(ans,calcMaxArea(temp,cols))
    return ans

matrix = [
    ["1","0","1","0","0"],
    ["1","0","1","1","1"],
    ["1","1","1","1","1"],
    ["1","0","0","1","0"]
    ]
print(maximalRect(grid=matrix))