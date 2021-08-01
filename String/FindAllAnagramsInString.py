#https://leetcode.com/problems/find-all-anagrams-in-a-string/
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
    #print(dic,counter)
    start = 0
    end = 0
    n = len(txt)
    ans = []
    while(end<n):
        currentletter = txt[end]
        if currentletter in dic:
            if dic[currentletter]>0:
                counter -= 1
            dic[currentletter]-=1
            

        if(end -start +1 == windowSize):
            if(counter==0):
                ans.append(start)
            if(txt[start] in dic):
                if(dic[txt[start]]>=0):
                    counter+=1
                dic[txt[start]]+=1
            
            #print(start,end,ans)    
            start+=1
        end+=1
    return ans

txt = "cbaebabacd"
pat = "abc"

print(CountAnagrams(pat,txt))