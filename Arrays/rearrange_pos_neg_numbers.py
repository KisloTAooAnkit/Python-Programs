#https://www.geeksforgeeks.org/move-negative-numbers-beginning-positive-end-constant-extra-space/
def rearrange(arr):
    n= len(arr)
    low = 0
    high = n-1
    mid = 0

    while(mid<=high):
        val = arr[mid]
        if(val<0):
            arr[mid],arr[low] = arr[low],arr[mid]
            mid+=1
            low+=1
        else:
            arr[mid],arr[high] = arr[high],arr[mid]
            high-=1
        
    
arr=[-12, 11, -13, -5, 6, -7, 5, -3, -6]

rearrange(arr)
print(arr)