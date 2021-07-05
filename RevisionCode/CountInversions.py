def count(arr):
    if(len(arr)>1):
        mid = len(arr)//2
        L = arr[:mid]
        R = arr[mid:]
        leftans = count(L)
        rightans = count(R)
        currans = mergeCount(L,R,arr)
        return currans + leftans + rightans
    else:
        return 0
    


def mergeCount(L,R,arr):
    i=0
    j=0
    k=0
    result = 0
    while(i<len(L) and j <len(R)):
        if(L[i]<=R[j]):
            arr[k] = L[i]
            i+=1
            k+=1

        elif(R[j]<L[i]):
            arr[k] = R[j]
            result += len(L) - i
            j+=1
            k+=1

    
    while(i<len(L)):
        arr[k] = L[i]
        k+=1
        i+=1

    while(j<len(R)):
        arr[k] = R[j]
        k+=1
        j+=1

    return result


arr = [10, 10, 10]
print(count(arr))

