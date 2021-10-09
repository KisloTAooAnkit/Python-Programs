def maximumSwap(num):
    arr = [int(x) for x in str(num)]
    dic = dict()
    for idx,key in enumerate(arr):
        dic[key] = idx
    n = len(arr)
    for index,value in enumerate(arr):
        for j in range(9,value,-1):
            if j in dic and dic[j]>index:
                arr[index],arr[dic[j]] = arr[dic[j]],arr[index]
                return int("".join(map(str,arr)))
    return int("".join(map(str,arr)))

n = 115
print(maximumSwap(n))