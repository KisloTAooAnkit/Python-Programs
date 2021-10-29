import sys

def helper(word,idx,n,ans,count):
    if isValid(word,n):
        if ans: 
            if ans[-1][0] == count:
                ans.append((count,"".join(word)))
            elif ans[-1][0] > count:
                ans.clear()
                ans.append((count,"".join(word)))
        else:
            ans.append((count,"".join(word)))
        return
    if idx >= n:
        return 
    cache = word[idx]
    word[idx] = ""
    helper(word,idx+1,n,ans,count+1)
    word[idx] = cache
    helper(word,idx+1,n,ans,count)
    return

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

def removeInvalidParenthesis(s):
    ans = []
    word = list(s)
    helper(word,0,len(word),ans,0)
    dic = dict()
    res = []
    while ans:
        key,val = ans.pop()
        if val not in dic:
            res.append(val)
            dic[val] = 1
    return res
    
s = ")("
removeInvalidParenthesis(s)