import math
def findDup(arr):
    for i in range(0,len(arr)):
        if arr[abs(arr[i])] >0:
            arr[abs(arr[i])] = - arr[abs(arr[i])]
        
        else:
            return abs(arr[i])
        

arr = [1,3,4,3,2] 

print(findDup(arr))