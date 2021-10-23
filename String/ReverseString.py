from collections import deque
def reverseWords(s):
    q = deque()
    n = 0
    for val in s:
        if n>0 and val == " " and q[-1] == " ":
            continue
        q.append(val)
        n +=1
    while(q and q[-1] == " "):
        q.pop()
    
    while(q and q[0] == " "):
        q.popleft()
    
    ans = []
    while q :
        ans.append(q.pop())
    return "".join(ans)

s = "the sky is blue"

print(reverseWords(s))
    
    
            