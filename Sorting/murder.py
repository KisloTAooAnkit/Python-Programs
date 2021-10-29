#Spoj Question
def mergeSortMurder(arr,ans):
    if len(arr)<=1:
        return
    
    mid = len(arr)//2
    L = arr[:mid]
    R = arr[mid:]
    mergeSortMurder(L,ans)
    mergeSortMurder(R,ans)
    merge(arr,L,R,ans)
    
    
def merge(arr,L,R,ans):
    i , j ,k = 0,0,0
    n1 = len(L)
    n2 = len(R)
    while(i<n1 and j < n2):
        
        if L[i] >= R[j]:
            arr[k] = R[j]
            j+=1
            k+=1
        elif(L[i]<R[j]):
            ans[0] += (n2 - j)*L[i]
            arr[k] = L[i]
            i+=1
            k+=1
    while(i<n1):
        
        arr[k] = L[i]
        k +=1
        i+=1
    while(j<n2):
        arr[k] = R[j]
        k+=1
        j+=1
        


    
arr = [1,2,3,4,5,6,5]
ans = [0]
mergeSortMurder(arr,ans)
print(ans,arr)
    
    