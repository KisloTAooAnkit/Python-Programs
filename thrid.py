from collections import defaultdict as dict
from bisect import bisect_left,bisect_right


def platesBetweenCandles(s,queries):
    bar = "|"
    star = "*"
    n = len(queries)
    ans = [0]*n
    dic = dict(list)

    for idx,val in enumerate(s):
        if val == bar:
            dic[bar].append(idx)
        if val == star:
            dic[star].append(idx)
    

    for idx,query in enumerate(queries):
        left,right = query
        leftBar = bisect_left(dic[bar],left)
        rightBar = bisect_right(dic[bar],right)-1

        stars = bisect_right(dic[star],dic[bar][rightBar]) - bisect_right(dic[star],dic[bar][leftBar])
        ans[idx] = stars
    return ans
