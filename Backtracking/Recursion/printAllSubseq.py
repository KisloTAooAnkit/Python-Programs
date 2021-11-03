def subseq(s,ans,currword):
    if len(s) == 0:
        ans.appe0nd(currword)
    
        return

    subseq(s[1:],ans,currword + s[0])
    subseq(s[1:],ans,currword)
    return

def subSeq2_0(s,output):
    if len(s) == 0:
        output.append("")
        return 1
    ans = subSeq2_0(s[1:],output)
    for i in range(ans):
        newWord = s[0] + output[i]
        output.append(newWord)
    return 2*ans


ans = []
s = "abc"
subSeq2_0(s,ans)
print(ans)