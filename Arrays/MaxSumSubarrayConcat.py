#https://www.codingninjas.com/codestudio/guided-paths/data-structures-algorithms/content/118820/offering/1381873

import sys
def KadanesReturnArray(arr,n):
    s,e = 0,0
    beg = 0
    best = -sys.maxsize
    currsum = -sys.maxsize
    for i in range(n):
        currsum = arr[i] + currsum
        if(currsum<arr[i]):
            currsum = arr[i]
            beg=i
            
        if(currsum>best):
            best = currsum
            s= beg
            e = i
    print(arr[s:e+1])
    return s,e,best

def maxSubSumKConcat(arr,n,k):
    si,ei,ans = KadanesReturnArray(arr,n)
    nonContriEleSum = sum(arr[0:si]) + sum(arr[ei+1:n])

    print(ans,nonContriEleSum)


    result = (ans*k) - abs(nonContriEleSum*(k-1))
    return result


arr =[-2,13,-4,-2,1,5,6]


print(maxSubSumKConcat(arr,len(arr),3)) 


    




