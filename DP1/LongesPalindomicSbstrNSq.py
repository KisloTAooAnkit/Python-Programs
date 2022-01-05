
def expandAroundCenter(s,start,end):
    
    while(start>=0 and end < len(s) and s[start] == s[end]):
        start -=1
        end +=1
    
    return (start+1,end-1)

def longesPalSubstr(s):
    n = len(s)
    globalLen = 0
    start = 0
    end = 0
    for i in range(n):
        s1,e1 = expandAroundCenter(s,i,i)
        s2,e2 = expandAroundCenter(s,i,i+1)
        if e1-s1+1 > globalLen:
            start = s1
            end = e1
            globalLen = e1 -s1 +1
        if e2 - s2 +1 > globalLen:
            start = s2
            end = e2
            globalLen = e2 - s2 +1
    
    return s[start:end+1]


a ="cbbd"
print(longesPalSubstr(a))

        
            


        
    
    