#https://leetcode.com/problems/single-element-in-a-sorted-array/
def singleNonDuplicate(arr):
    start = 0
    n = len(arr)
    end = n-1
    if(n==1):
        return arr[0]
    if(n==2):
        if(arr[0]==arr[1]):
            return -1
        else:
            return arr[0]
    while(start<=end):
        mid = start + (end-start)//2
        left = False 
        right = False
        leftcount = mid - start
        rightcount = end - mid
        if( (mid==0 and arr[mid] == arr[mid+1]) or (mid+1<n) and (arr[mid] == arr[mid+1])):
            right = True
            rightcount = end - mid+1

        elif((mid==n-1 and arr[mid] == arr[mid-1]) or (mid-1>=0) and (arr[mid] == arr[mid-1])):
            left = True
            leftcount = mid-1 - start

        if(not left and not right):
            return arr[mid]
        
        if(leftcount%2 !=0):
            end = mid-2 if left else mid-1
        
        elif(rightcount%2 !=0):
            start = mid+2 if right else mid+1

    return -1

arr = [1,1,2,3,3]
print(singleNonDuplicate(arr))
        
        

