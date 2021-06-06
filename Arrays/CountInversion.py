
#https://practice.geeksforgeeks.org/problems/inversion-of-array-1587115620/1
"""
approach : Merge sort 
Find inversion of left part
Find inversion of right part
find inversion of merging
while merging do the same thing as normal merge sort but in the case of Left[i]>right[j] we know this is inversion 
then we increase the inversion count by len(L) - i (as array is sorted if ith index is in inversion then i+1 ... len(L) will
also be in inversion to right[j] element)
"""

def countInversion(arr):
    if(len(arr)>1):
        mid = len(arr)//2
        L = arr[:mid]
        R= arr[mid:]
        leftans = countInversion(L)
        rightans = countInversion(R)
        current_ans = countVal(arr,L,R)
        return leftans+rightans+current_ans
    else:
        return 0




def countVal(arr,L,R):
    count = 0
    i =0 
    j=0
    k=0
    while(i<len(L) and j < len(R)):
        if(L[i]<=R[j]):
            arr[k] = L[i]
            i+=1
            k+=1
        elif(R[j]<L[i]):
            arr[k] = R[j]
            j+=1
            k+=1
            count += len(L) - i 
        
    while(i<len(L)):
        arr[k] = L[i]
        i+=1
        k+=1

    while(j<len(R)):
        arr[k] = R[j]
        j+=1
        k+=1
    return count




arr= [4,3,2,1]
print(countInversion(arr))