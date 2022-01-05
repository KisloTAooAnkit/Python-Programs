
def expandAndCount(s,start,end):
    ans = 0
    while(start>=0 and end < len(s) and s[start] == s[end]):
        ans+=1
        start -=1
        end +=1
    return ans
    


def countSubstr(s):
    ans = 0
    for i in range(len(s)):
        a = expandAndCount(s,i,i)
        b = expandAndCount(s,i,i+1)
        ans += a + b
        
    return ans
