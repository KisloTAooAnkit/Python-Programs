import sys
def minWindowSubstring(s,t):
    cnt = 0
    dic = dict()
    start = 0
    end = 0
    windowSize = len(t)
    print(windowSize)
    n = len(s)
    ans = ""
    ansLen = sys.maxsize
    coord = ()

    # if(len(s)<len(t)):
    #     return ""

    for i in t:
        if(i not in dic):
            dic[i] = 1
        else:
            dic[i]+=1

    while(end<n):
        val = s[end]
        if(s[end] in dic):
            if(dic[s[end]]>0):
                cnt+=1
            dic[s[end]] -= 1
 
        
        while(cnt == windowSize):
            if(ansLen >= end - start +1):
                ansLen = end - start +1
                coord = (start,end)
                ans = s[start:end+1]
                print(coord)
            if(s[start] in dic):
                dic[s[start]] +=1
                if(dic[s[start]]>0):
                    cnt-=1
            start+=1
        end+=1
    # print(coord)
    return ans

s = "ADOBECODEBANC" 
t = "ABC"

# s="aa" 
# t="aa"


print(minWindowSubstring(s,t))
