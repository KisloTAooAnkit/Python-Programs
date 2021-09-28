
#https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/
def findMin(arr):
    start = 0
    end = len(arr) -1
    n = end+1
    while(start<=end):
        if(arr[start]<arr[end]):
            return start
        
        mid = start + (end-start)//2

        prev = (mid - 1 + n) % n
        nxt = (mid+1) %n

        if(arr[mid]<arr[prev] and arr[mid]<arr[nxt]):
            return mid

        elif(arr[mid]<arr[start]):
            end = mid-1
        
        elif(arr[mid]>arr[end]):
            start = mid+1

arr = [3,3,3,1]

print(findMin(arr))
    
