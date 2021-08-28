import random
#https://leetcode.com/problems/kth-largest-element-in-an-array/ 
def kthLargestElement(arr,kth):
    left = 0
    right = len(arr) -1 
    k = len(arr) - kth
    while(left<=right):
        part_idx = quickPartition(arr,left,right)

        if(part_idx == k):
            return arr[part_idx]

        if(part_idx>k):
            right = part_idx-1
        elif(part_idx<k):
            left = part_idx+1

    return -1
    


def quickPartition(arr,low,high):
    pivot_idx = low
    pivot = arr[pivot_idx]

    while(low<high):
        while(low < len(arr) and arr[low]<=pivot):
            low+=1

        while(arr[high]>pivot):
            high-=1
        
        if(low<high):
            arr[low],arr[high] = arr[high],arr[low]

    arr[pivot_idx],arr[high] = arr[high],arr[pivot_idx]

    return high


arr = [1,4,41,41,41,12,13,13,1]
k = 4

print(kthLargestElement(arr,k))
