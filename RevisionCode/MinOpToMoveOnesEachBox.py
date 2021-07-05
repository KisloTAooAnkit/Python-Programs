def minOperations(arr):
    n = len(arr)
    numberofOnes =0
    ans = [0]*n
    res = 0

    for i in range(n-2,-1,-1):
        buffer  =1 if(arr[i+1] == "1") else 0
        numberofOnes = numberofOnes + buffer
        res  = numberofOnes + res
        ans[i] +=res
    
    print(ans)

    res = 0
    numberofOnes =0


    for i in range(1,n):
        buffer  =1 if(arr[i-1] == "1") else 0
        numberofOnes = numberofOnes + buffer
        res = numberofOnes + res
        ans[i] += res


    return ans


print(minOperations("111111"))


