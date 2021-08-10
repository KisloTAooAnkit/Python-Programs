def search(pat,txt):
    patterDic = dict()
    for i in pat:
        if(i not in patterDic):
            patterDic[i] = 1
        else:
            patterDic[i] +=1
    count = len(patterDic)
    windowSize = len(pat)
    ans = 0
    n = len(txt)
    start = 0
    end = 0
    while(end<n):
        if(txt[end] in patterDic):
            patterDic[txt[end]] -=1
            if(patterDic[txt[end]]==0):
                count -=1
            else:
                patterDic[txt[end]] =0 
        if(end-start+1 == windowSize):
            if(count == 0):
                ans+=1
            if(txt[start] in patterDic):
                txt[start]+=1
                if(txt[start] == 1):
                    count+=1
            start+=1
        end+=1
        
                
