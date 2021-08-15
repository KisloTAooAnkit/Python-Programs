def PermCaseChange(inp,temp,ans):
    if(len(inp)==0):
        ans.append(temp)
        return
    
    if(not inp[0].isdigit()):
        PermCaseChange(inp[1:],temp + inp[0].upper(),ans)
        PermCaseChange(inp[1:],temp+inp[0].lower(),ans)
        return 
    PermCaseChange(inp[1:],temp+inp[0],ans)
    return

ans = []
s = "A1B2C"

PermCaseChange(s,"",ans)
print(ans)