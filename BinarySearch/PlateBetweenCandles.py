from bisect import bisect_left,bisect_right
from collections import defaultdict as dict

     


def plateBetweenCandles(s,queries):
    dic = dict(list)
    bar = "|"
    star = "*"
    print(dic)
    starCount = 0
    candelCount = 0
    for idx,val in enumerate(s):
        if val == "*":
            starCount+=1
        else:
            candelCount+=1
        dic[val].append(idx)
    
    ans = []
    for left,right in queries:

        leftCIdx = bisect_left(dic[bar],left)
        rightCIdx = bisect_right(dic[bar],right) -1

        if leftCIdx >=rightCIdx:
            ans.append(0)
            continue
        leftcandle = dic[bar][leftCIdx]
        rightcandle = dic[bar][rightCIdx]

        a = bisect_right(dic[star],leftcandle)
        b = bisect_right(dic[star],rightcandle) 

        ans.append(b-a)

    return ans

s= "***|**|*****|**||**|*"
q = [[1,17],[4,5],[14,17],[5,11],[15,16]]
print(plateBetweenCandles(s,q))