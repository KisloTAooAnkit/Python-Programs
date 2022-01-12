def findMaxlenZeroSubarray(arr,n):
    s = 0
    maxLen = 0
    dic = {0:-1}
    for i in range(n):
        s += arr[i]
        if s in dic:
            maxLen = max(maxLen,i-dic[s])
        else:
            dic[s] = i
    return maxLen


def solve(matrix):

    n = len(matrix)
    m = len(matrix[0])
    ans = 0
    arr = [0]*n

    for i in range(m):
        for j in range(i,m):
            if i == j:
                for k in range(n):
                    arr[k] = matrix[k][i]
            else:
                for k in range(n):
                    arr[k] += matrix[k][j]
            res = findMaxlenZeroSubarray(arr,n)
            ans = max(res*(j-i+1) ,ans )
    return ans


arr = [
        [9,7,16,5],
        [1,-6,-7,3],
        [1,8,7,9],
        [7,-2,0,10]
    ]

print(solve(arr))

 
                