def isValidSubstr(s):
    stack = []
    for i in s:
        
        if i == "(":
            stack.append(i)
        elif i == ")":
            if not stack:
                return False
            else:
                stack.pop()
    return not stack

def dfs(n,s,curr,idx,open,close,ans):
    if n == 0:
        if open > 0 or close >0:
            return
        else:
            if isValidSubstr(curr):
                ans.add(curr)
            return
    
    val = s[idx]
    if val == "(" and open >0:
        dfs(n-1,s,curr,idx+1,open-1,close,ans)
    elif val == ")" and close >0:
        dfs(n-1,s,curr,idx+1,open,close-1,ans)
    dfs(n-1,s,curr+val,idx+1,open,close,ans)
    return


def solve(s):
    invalidOpen = 0
    invalidClose = 0
    balance = 0
    n = len(s)
    for i in range(n):
        if s[i] == "(":
            balance +=1
        elif s[i] == ")":
            balance -=1
        
        if balance < 0:
            invalidClose +=1
            balance =0
    balance = 0
    for i in range(n-1,-1,-1):
        if s[i] == ")":
            balance +=1
        elif s[i] == "(":
            balance -=1
        if balance <0:
            invalidOpen +=1
            balance = 0
    ans = set()
    dfs(n,s,"",0,invalidOpen,invalidClose,ans)
    return ans

s =")("

print(solve(s))