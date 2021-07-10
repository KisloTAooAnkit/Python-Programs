def kthSmallest(matrix, k):
    n= len(matrix)
    m = n-1
    k-=1
    val = k
    x=0

    while(val>m):
        val -= n
        x+=1
    
    return matrix[x][val]

matrix = [[1,5,9],[10,11,13],[12,13,15]]
k = 1



print(kthSmallest(matrix,k))