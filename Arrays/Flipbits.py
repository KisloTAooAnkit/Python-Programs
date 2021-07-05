
#https://practice.geeksforgeeks.org/problems/flip-bits0240/1

def flipBits(arr, n): 
    # Write your code here
    onbias = 0
    zerobias = 0
    ans = 0
    for i in range(n):
        if(arr[i] == 1):
            onbias +=1
            zerobias -=1
        else:
            zerobias+=1
        
        ans = max(zerobias,ans)
        zerobias = max(zerobias,0)
    
    return onbias+ans
         
            

arr= [0,0,1,0,0]
print(flipBits(arr,len(arr)))

