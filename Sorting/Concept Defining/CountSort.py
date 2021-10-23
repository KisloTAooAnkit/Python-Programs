def countSort(arr):
    n = len(arr)
    mn = min(arr)
    mx = max(arr)
    freq = [0]*(mx-mn+1)
    ans = [0]* n
    for _,val in enumerate(arr):
        freq[val-mn] +=1
    
    #generate prefix sum
    for i in range(1,mx-mn+1):
        freq[i] = freq[i] + freq[i-1]
    for i in range(mx-mn+1):
        freq[i] -=1
        
    
    for i in range(n-1,-1,-1):
        val = arr[i]
        idx = freq[val-mn]
        ans[idx] = val
        freq[val-mn] -=1
    return ans



arr = [4,2,1,5,2,2,4,6]

print(countSort(arr))

