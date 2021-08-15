def countAndSay(n):
    s = str(n)
    start = 0
    n = len(s)
    end = 0
    ans = ""
    while(end<n):
        prevNum = s[start]
        while(s[end]==prevNum):
            end+=1
        windowSize = str(end-start)
        ans = ans + windowSize + prevNum
        start = end
    return ans

#n = 
print(countAndSay)