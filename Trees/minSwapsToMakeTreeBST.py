def inorder(arr,inarr,i):
    if i >= len(arr):
        return
    
    inorder(arr,inarr,2*i + 1)
    inarr.append(arr[i])
    inorder(arr,inarr,2*i + 2)
    return

def minSwaps(arr):
    #PHASE -1 
    inarr = []
    inorder(arr,inarr,0)

    #PHASE 2
    arr.sort()
    dic = dict()
    for idx,val in enumerate(inarr):
        dic[val] = idx
    i,j = 0,0
    ans = 0
    while(i<len(arr)):
        if arr[i] != inarr[j]:
            ans += 1
            swappingIdx = dic[arr[i]]
            dic[inarr[j]] = swappingIdx
            dic[arr[i]] = i
            inarr[j],inarr[swappingIdx] = inarr[swappingIdx],inarr[j]
        if arr[i] == inarr[j]:
            i+=1
            j+=1
    return ans

arr = [1 ,2 ,3]# ,4 ,5 ,6, 7]
print(minSwaps(arr))
