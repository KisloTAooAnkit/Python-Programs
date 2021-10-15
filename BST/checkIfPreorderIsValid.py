import sys
def constructTree(arr,idx,n,low,high):
    if idx[0]>=n or low>high or arr[idx[0]] < low or arr[idx[0]] > high:
        return
    
    val = arr[idx[0]]
    idx[0] +=1

    if(idx[0] < n and arr[idx[0]]<val):
        constructTree(arr,idx,n,low,val-1)
    
    if(idx[0] < n and arr[idx[0]]>val):
        constructTree(arr,idx,n,val+1,high)
    return


def ifPreorderIsValid(arr):
    n = len(arr)
    idx = [0]
    low = -sys.maxsize
    high = sys.maxsize
    constructTree(arr,idx,n,low,high)
    if idx[0] <n:
        return False
    return True

arr = [2,4,1]
print(ifPreorderIsValid(arr))