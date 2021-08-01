#https://practice.geeksforgeeks.org/problems/count-occurences-of-anagrams5839/1
def CountAnagrams(pat,txt):
    dic = dict()
    counter = 0
    for i in pat:
        counter +=1
        if i in dic:
            dic[i] +=1
        else:
            dic[i] = 1
    windowSize = counter
    print(dic,counter)
    start = 0
    end = 0
    n = len(txt)
    ans = 0
    while(end<n):
        currentletter = txt[end]
        if currentletter in dic:
            if dic[currentletter]>0:
                counter -= 1
            dic[currentletter]-=1
            

        if(end -start +1 == windowSize):
            if(counter==0):
            
                ans +=1
            if(txt[start] in dic):
                if(dic[txt[start]]>=0):
                    counter+=1
                dic[txt[start]]+=1
            
            #print(start,end,ans)    
            start+=1
        end+=1
    return ans

txt = "kkkkkkkk"
pat = "kkkk"

print(CountAnagrams(pat,txt))