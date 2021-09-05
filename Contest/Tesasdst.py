def solution(n,arr,windowSize):
    sample = arr[:]
    sample.sort()
    starting = n-windowSize
    mydic = dict()
    for i in range(starting,n):
        if sample[i] not in mydic:
            mydic[sample[i]] = 1
        else:
            mydic[sample[i]] += 1
    res = []
    for i in range(0,n):
        if arr[i] in mydic and mydic[arr[i]] > 0:
            res.append(arr[i])
            mydic[arr[i]] -=1
    
    return res