def sol(arr,k):
    n = len(arr)
    prefix = [0]*n
    prefix[0] = arr[0]
    dic = dict()
    dic[0] = 1
    for i in range(1,n):
        prefix[i] = arr[i] + prefix[i-1]
    ans = 0
    for i in range(n):
        val = prefix[i]%k
        if val in dic:
            ans += dic[val]
            dic[val] +=1
        else:
            dic[val] = 1
    return ans