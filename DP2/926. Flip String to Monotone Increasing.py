def minFlip(s):
    arr = list(s)
    
    n = len(arr)
    zero = [0]*n
    ones = [0]*n
    ones[0] = 1 if arr[0] == "1" else 0
    zero[n-1] = 1 if arr[n-1] == "0" else 0
      
    for i in range(1,n):
        ones[i] = ones[i-1] +1 if arr[i] == "1" else ones[i-1]
    
    for i in range(n-2,-1,-1):
        zero[i] = zero[i+1] +1 if arr[i] == "0" else zero[i+1]
    
    
    ans = float("inf")
    for i in range(0,n):
        prev = 0 if i-1 < 0 else ones[i-1]
        nxt = 0 if i+1 >= n else zero[i+1]
        ans = min(prev+nxt,ans)
    return ans

############################# O(1) space approach ##########################
def minFlipOpt(s):
    arr = list(s)
    n = len(arr)
    zero,ones = 0,0
    #count the problematic zeros in right side
    for i in range(n-1,-1,-1):
        if arr[i] == "0":
            zero +=1
    ans = float("inf")
    
    for i in range(n):
        if arr[i] == "0":
            #since we have current idx as zero there is one 
            # less zero on right side
            zero-=1
            ans = min(ans,zero+ones)
        if arr[i] == "1":
            ans = min(ans,ones+zero)
            #after encountring this one it will go on left side and create
            #problem for us so we update after calc the min
            ones+=1
    return ans 


s ="00011000"
print(minFlip(s))