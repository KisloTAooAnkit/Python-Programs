import sys
from collections import deque

def isValid(arr,n):
    count = 0
    for i in range(n):
        if arr[i] == "(":
            count +=1
        if arr[i] == ")":
            
            if count == 0:
                return False
            count -=1
    return count == 0

#BFS
def removeInvalidParenthesis(s):
    ans = []
    hashmap = set()
    currLen = 0
    q = deque()
    n = len(s)
    q.append((s,n,0))

    while(q):
        arr,n,idx = q.popleft()
        if isValid(arr,n) and currLen <= n:
            currLen = n
            ans.append(arr)

        else:   
            if idx <n and n >= currLen:
                q.append((arr,n,idx+1))
                if (arr[idx] == "(" or arr[idx] == ")") :
                    val = arr[:idx] + arr[idx+1:]
                    if val not in hashmap:
                        q.append((val,n-1,idx))
                        hashmap.add(val)
    return ans


#Backtracking DFS

def findNImbalancedBrackets(s):
    stack = []
    for i in s:
        if i == ")":
            if stack and stack[-1] == "(":
                stack.pop()
            else:
                stack.append(i)
        elif i == "(":
            stack.append(i)
    return len(stack)

def dfs(word,n,minremv,hashmap,ans):
    if minremv == 0:
        if isValid(word,n):
            ans.append(word)
            return
    if n < minremv:
        return
    
    for i in range(n):
        if word[i] == "(" or word[i] == ")":
            sbstr = word[:i] + word[i+1:]
            if sbstr not in hashmap:
                hashmap.add(sbstr)
                dfs(sbstr,n-1,minremv-1,hashmap,ans)
    return

def removeInvalidParenthesisDFS(s):
    hashmap = set()
    ans = []
    no_of_unbalanced_bracket = findNImbalancedBrackets(s)
    dfs(s,len(s),no_of_unbalanced_bracket,hashmap,ans)
    print(ans)



    
s = "(a)())()"
removeInvalidParenthesisDFS(s)
##dfsdfsdf
