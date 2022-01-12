def maxZerosumSubarray(arr,n):
    prefix = 0
    dic = {0:-1}
    ans = 0
    for i in range(n):
        prefix += arr[i]
        if prefix in dic:
            ans = max(ans,i-dic[prefix])
        else:
            dic[prefix] = i
    return ans


def findLargestRect(matrix):

    rows = len(matrix)
    cols = len(matrix[0])

    arr = [0]*rows
    ans = 0
    for i in range(rows):
        for j in range(cols):
            if matrix[i][j] == 0:
                matrix[i][j] = -1
    for i in range(cols):
        for j in range(cols):
            if i == j:
                for k in range(rows):
                    arr[k] = matrix[k][i]
            else:
                for k in range(rows):
                    arr[k] += matrix[k][j]
        
            windowSize = j-i +1
            ans = max(ans,windowSize*maxZerosumSubarray(arr,rows))
    return ans



arr = [
    [0,0,1,1],
    [0,1,1,0],
    [1,1,1,0],
    [1,0,0,1]
    ]

print(findLargestRect(arr))


