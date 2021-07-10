#https://leetcode.com/problems/how-many-numbers-are-smaller-than-the-current-number/


def smallerNumbersThanCurrent(arr):
    n = len(arr)
    copy = arr[:]
    copy.sort()
    dic = dict()
    for i in range(n):
        if(copy[i] in dic):
            dic[copy[i]] = min(dic[copy[i]] ,i)
        else:
            dic[copy[i]] = i
    
    for i in range(n):
        copy[i] = dic[arr[i]]
    return copy


arr =[7,7,7,7]

print(smallerNumbersThanCurrent(arr))
