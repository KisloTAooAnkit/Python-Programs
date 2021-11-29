def makeMin(s,k):
    stack = list()
    n = len(s)
    for i in range(0,n):
        curr = s[i]
        while(stack and k>0 and stack[-1]>curr):
            stack.pop()
            k-=1
        if curr == "0" and not stack:
            continue
        stack.append(curr)
    while(k):
        stack.pop()
        k-=1

    ans =  "".join(stack) 
    return ans if ans != "" else "0"


s = "110200"
k = 2
print(makeMin(s,k))