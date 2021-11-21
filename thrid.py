#arr = [1,2,4,4,55]
# n= 5
def maxDistance(arr):
    n = len(arr)
    i = 0
    ans = 0
    while(i<n):  
        if arr[0] != arr[n-1]:
            return n-1
        elif arr[0] != arr[i]:
            ans +=1 
        elif arr[0] == arr[i]:
            ans+=1
        i+=1
    return ans
    
arr = [1,1,1,6,1,1,1]
print(maxDistance(arr))