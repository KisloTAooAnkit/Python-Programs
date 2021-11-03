def removeDupli(s,idx,n,arr):
    if idx == n:
        arr.append("")
        return ""
    
    ans = removeDupli(s,idx+1,n,arr)
    if ans == s[idx]:
        return ans
    else:
        arr.append(s[idx])
        return s[idx]

def removeDuplicates(s):
    ans = []
    removeDupli(s,0,len(s),ans)
    print("".join(ans[::-1]))

s = "abcd"
removeDuplicates(s)
    