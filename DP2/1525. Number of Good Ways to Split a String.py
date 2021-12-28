from collections import defaultdict
def ans(s):
    n = len(s)
    prefix = [0]*n
    suffix = [0]*n
    dic = defaultdict(lambda : 0)
    dic[s[0]] = 1
    prefix[0] = 1
    suffix[n-1] = 1
    for i in range(1,n):
        if s[i] not in dic:
            dic[s[i]] = 1
            prefix[i] = prefix[i-1] +1
        else:
            prefix[i] = prefix[i-1]
        
    for key in dic:
        dic[key] = 0
    dic[s[n-1]] = 1
    for i in range(n-2,-1,-1):
        if dic[s[i]] == 0:
            suffix[i] = suffix[i+1] +1
            dic[s[i]] =1
        else:
            suffix[i] = suffix[i+1]
    res = 0
    for i in range(0,n-1):
        if prefix[i] == suffix[i+1]:
            res+=1
    return res

s = "aaaaa"

print(ans(s))