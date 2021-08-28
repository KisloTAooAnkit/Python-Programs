
def merge(arr,L,R):
    i ,j,k=0,0,0
    while(i<len(L) and j<len(R)):
        if(L[i]>=R[j]):
            arr[k] = R[j]
            j+=1
            k+=1
        elif(L[i]<R[j]):
            arr[k] = L[i]
            i+=1
            k+=1
    while(i<len(L)):
        arr[k] = L[i]
        k+=1
        i+=1

    while(j<len(R)):
        arr[k] = R[j]
        k+=1
        j+=1
        

def mergeSort(arr):
    if(len(arr)>1):
        mid = len(arr)//2
        L = arr[:mid]
        R = arr[mid:]
        mergeSort(L)
        mergeSort(R)
        merge(arr,L,R)
    


arr = [9,8,8,8,9,99,99,99,999,9,99,555,99,00,8]
mergeSort(arr)
print(arr)