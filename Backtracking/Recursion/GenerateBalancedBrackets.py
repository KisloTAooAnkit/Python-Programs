def genParenthesis(n):
    
    ans = set()
    helper(ans,"",n,n)
    return list(ans)


def helper (ans,temp,opening,closing):
    if(opening==0 and closing == 0):
        ans.add(temp)
        return

    if(opening>0):
        helper(ans,temp + "(",opening-1,closing)
    if(closing>opening):
        helper(ans,temp+")",opening,closing-1)
    return



n = 3
print(genParenthesis(n))