#https://leetcode.com/problems/longest-consecutive-sequence/submissions/


def longestConsecutive(arr):
    dic = dict()
    n = len(arr)
    maxlen = 0
    for i in range(0,n):
        if arr[i] not in dic:
            dic[arr[i]] = True

    
    for key in dic:
        if key-1 in dic:
            dic[key] = False

    
    for key in dic:
        if(dic[key] == True):
            startingkey = key
            currlen = 0
            while(startingkey in dic):
                startingkey +=1
                currlen +=1
            maxlen = max(currlen,maxlen)
    
    return maxlen


arr = [0,3,7,2,5,8,4,6,0,1]
print(longestConsecutive(arr))

    