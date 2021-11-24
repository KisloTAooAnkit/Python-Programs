def helper(number,factor,dic):
    if number == 0:
        return 0
    
    if number in dic:
        return 0

    dic[number%factor] = 1
    ans1 = number%factor + helper(number//factor,factor,dic)
    ans2 = helper(number,factor*10,dic)
    return ans1 + ans2

def substrings(string):
    num = int(string)
    dic = dict()
    return helper(num,10,dic)


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