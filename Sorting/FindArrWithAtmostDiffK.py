#https://www.geeksforgeeks.org/searching-array-adjacent-differ-k/
import math
def findK(arr,target,k):
    idx = 0
    n = len(arr)
    while(idx<n):
        if(arr[idx]==target):
            return idx

        diff = abs(arr[idx]-target)
        x =  math.ceil(diff/k)
        idx = idx+x
    return -1

arr = [20,40,50,70,70,60,80]
t = 77
k =20
print(findK(arr,t,k))