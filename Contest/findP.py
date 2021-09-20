def solution(arr):
    n = len(arr)
    dic = dict()
    for i in range(n):
        if arr[i] not in dic:
            dic[arr[i]] = 1
        else:
            dic[arr[i]] +=1
    arr.sort()

    ans = []
    for i in range(n):
        if dic[arr[i]] > 0:
            dic[arr[i]] -=1
            if arr[i]*2 in dic and dic[arr[i]*2]>0:
                dic[arr[i]*2] -=1
                ans.append(arr[i])
            else:
                dic[arr[i]] +=1
    for keys in dic:
        if dic[keys] > 0:
            return []

    return ans

a = [0]
print(solution(a))   

        
