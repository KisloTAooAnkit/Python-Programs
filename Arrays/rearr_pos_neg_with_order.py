
'''
approach yeh hai : merge sort ka idea use karenge .. sab same rahega array ko todne tak but jaise hi ham merge process 
chalu karenge thabhi og array mein
1: pehele left part ke sare -ve ko bharo
2: phir right part ke sare -ve ko bharo
3: phir left part ke sare +ve ko bharo
4: phir right part ke sare +ve ko bharo
TC = O(nlogn) SC = O(n)
'''


def solution(arr):
    if(len(arr)>1):
        mid = len(arr)//2
        l = arr[:mid]
        r = arr[mid:]
        solution(l)
        solution(r)
        merge(l,r,arr)
        
        
        
def merge(L,R,arr):
    i=0
    k=0
    left_len = len(L)
    right_len = len(R)
    
    #left ke negative no. ko og array mein bharo
    while(i<left_len):
        if(L[i]<0):
            arr[k] = L[i]
            k+=1
        i+=1
        
    #right ke negative no. ko og array mein bharo
    i=0
    while(i<right_len):
        if(R[i]<0):
            arr[k] = R[i]
            k+=1
        i+=1
    
    #left ke positive no. ko og array mein bharo
    i=0
    while(i<left_len):
        if(L[i]>=0):
            arr[k] = L[i]
            k+=1
        i+=1
    
    #right ke positive no. ko og array mein bharo

    i=0
    while(i<right_len):
        if(R[i]>=0):
            arr[k] = R[i]
            k+=1
        i+=1
    
         
arr = [-12 ,11, -13, -5 ,6 ,-7, 5, -3, -6]
arr1=[1,-1]
solution(arr1)
print(arr1)