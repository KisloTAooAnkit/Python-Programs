def checkSubaaray(arr,k):
    n = len(arr)
    prefix = [0]*n
    prefix[0] = arr[0]
    for i in range(1,n):
        prefix[i] = arr[i] + prefix[i-1]
    dic = dict()
    dic[0] = -1
    for i in range(n):
        val = prefix[i]%k
        if val in dic and i-dic[val]>1:
            return True
        else:
            dic[val] = min(i,dic.get(val,float("inf")))
    return False

arr = [5,0,0,0]

k = 3

print(checkSubaaray(arr,k))
        