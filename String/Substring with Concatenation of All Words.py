def findSubstring(s,words):
    dic = dict()
    for i in words:
        if i not in dic :
            dic[i]  = 1
        else:
            dic[i] +=1
    
    windowSize = len(words[0])
    n = len(s)
    start = 0
    end = 0
    count = len(words)
    m = count
    ans = []

    if not s or len(words) ==0:
        return []

    if(windowSize*count>n):
        return []

    for i in range(0,(n-windowSize*count)+1):
        start =i
        end = i+windowSize-1
        if(s[start:end+1] in dic):
            k = 0
            for i in range(0,m):
                flag =False
                piv1 = i*windowSize +start
                piv2 = piv1 + windowSize-1
                word = s[piv1:piv2+1]
                if(word in dic):
                    if(dic[word]>0):
                        dic[word] -=1
                        count -=1
                    else:
                        flag = True
                if(flag):
                    break
                k+=1
                
            if(count == 0):
                ans.append(start)
            
            for i in range(0,m):
                piv1 = i*windowSize +start
                piv2 = piv1 + windowSize-1
                if(k<=0):
                    break
                word = s[piv1:piv2+1]
                if(word in dic):
                    dic[word] +=1
                    count +=1
                k-=1

    
    return ans

                


s="wordgoodgoodgoodbestword"
words = ["word","good","best","good"]

print(findSubstring(s,words))