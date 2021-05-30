#https://leetcode.com/problems/move-zeroes/submissions/

"""logic : keep two pointers fast and slow swap 
if arr[fast] == 0 proceed ,
if arr[fast] != 0 swap fast with slow 
fast will increment as it is and slow will increment only while swapping hence 
slow pointer will maintain first 0 postion for next swap"""

def moveZeroes(arr):
    n= len(arr)
    slow = 0  
    for fast in range(n):
        if(arr[fast]!=0):
            arr[fast],arr[slow] = arr[slow],arr[fast]
            slow+=1
                
        
arr=[0,1,2,0,2,1,44,0,0,0,4]
moveZeroes(arr)
print(arr)