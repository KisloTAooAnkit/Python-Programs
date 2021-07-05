def sol(arr):
    if len(arr)>1:
        mid = len(arr)//2
        L = arr[:mid]
        R = arr[mid:]
        sol(L)
        sol(R)
        merge(L,R,arr)


def merge(L,R,arr):
    i=0
    j=0
    k=0
    for i in range(len(L)):
        if(L[i]<0):
            arr[k]=L[i]
            k+=1
    
    for j in range(len(R)):
        if(R[j] <0):
            arr[k] = R[j]
            k+=1
    for i in range(len(L)):
        if(L[i]>=0):
            arr[k]=L[i]
            k+=1
    
    for j in range(len(R)):
        if(R[j]>=0):
            arr[k] = R[j]
            k+=1


arr= [12 ,11, -13 ,-5 ,6 ,-7 ,5, -3, -6]
sol(arr)
print(arr)