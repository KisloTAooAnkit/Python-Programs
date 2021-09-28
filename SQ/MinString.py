def minValue(s, k):
    # code here
    dic = dict()
    for char in s:
        if char not in dic:
            dic[char] = 1
        else:
            dic[char] +=1
    
    dic = dict(sorted(dic.items(), key=lambda item: item[1] ,reverse=True))
    ans = 0
    for key in dic:
        if k>0:
            dic[key] -=1
            
            k-=1
        ans += dic[key] ** 2
    return ans

s = "aabcbcbcabcc"
print(minValue(s,3))