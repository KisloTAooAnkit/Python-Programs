"""
1:sort the matrix basis on cost col
2: Find min number or steps to make array strictly increasing for attractive array (LIS Variation)
"""
def minRemove(arr, n):
    LIS = [0 for i in range(n)]
    len = 0
    for i in range(n):
        LIS[i] = 1
    for i in range(1, n):
        for j in range(i):
            if (arr[i][0] > arr[j][0] and (i-j)<=(arr[i][0]-arr[j][0]) ):
                LIS[i] = max(LIS[i], LIS[j] + 1)
                 
        len = max(len, LIS[i])
    return (n - len)


def solution(arr,N):

    


    return minRemove(arr,N)

a = [[5 ,1 ,1, 5],
 [2 ,2, 2, 5],
 [3 ,3, 2, 5],
 [4 ,4 ,2, 5]]

print(solution(a,4))