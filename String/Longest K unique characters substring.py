#https://practice.geeksforgeeks.org/problems/longest-k-unique-characters-substring0853/1#

def longestKSubstr(s,k):
    mydict = dict()
    start = 0
    end = 0
    cnt = 0
    currentLength = 0
    ans = -1
    n= len(s)
    while(end<n):
        currtxt = s[end]
        if(currtxt not in mydict):
            cnt +=1
            mydict[currtxt] = 1
            
        else:
            mydict[currtxt]+=1
        
        if(cnt == k):
            currentLength = end - start +1
            ans = max(ans,currentLength)
        
        while(cnt>k):
            mydict[s[start]] -=1
            if(mydict[s[start]] == 0):
                mydict.pop(s[start])
                cnt-=1
            start+=1
     
        end+=1
    
    return ans

S = "aabacbebebe"
K = 3

print(longestKSubstr(S,K))