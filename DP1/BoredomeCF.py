from typing import Counter


def bordom(arr):
    dic = Counter(arr)
    freqArr = [(key,val) for key,val in dic.items()]
    freqArr.sort()
    n = len(freqArr)
    for i in range(n):
        val,freq = freqArr[i]
        dic[val] = max(
                        freq*val + dic.get(val-2,0),
                        dic.get(val-1,0)
                       )
    ans = 0
    for key in dic:
        ans = max(ans,dic[key])
    return ans
    
 
arr = [1,2,3,4,5]
print(bordom(arr))