def samAndSubstrings(string):
    ans = 0
    prev = 0
    for idx,val in enumerate(string):
        val = prev*10 + ((idx+1) * int(val))
        prev = val
        ans += val
    return ans

s = "123"
print(samAndSubstrings(s))