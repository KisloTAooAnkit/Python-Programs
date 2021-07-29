import sys
def maxProductDifference(arr):
    firstmax = -sys.maxsize
    secondmax = -sys.maxsize
    
    firstmin = sys.maxsize
    secondmin = sys.maxsize
    
    
    n= len(arr)
    
    for i in range(n):
        if(arr[i]>firstmax):
            secondmax = firstmax
            firstmax = arr[i]
        elif(arr[i]>secondmax):
            secondmax = arr[i]
        
        if(arr[i]<firstmin):
            secondmin = firstmin
            firstmin = arr[i]
        elif(arr[i]<secondmin):
            secondmin = arr[i]      
    
    print(firstmax,secondmax,firstmin,secondmin)
    
    return (firstmax*secondmax) - (firstmin*secondmin)

arr =  [4,2,5,9,7,4,8]
print(maxProductDifference(arr))