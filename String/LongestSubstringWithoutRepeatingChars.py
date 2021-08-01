#https://leetcode.com/problems/longest-substring-without-repeating-characters/

def lengthOfLongestSubstring(s):
    uniqueCount = 0
    mydic = dict()
    ans = 0
    start = 0
    end = 0
    n = len(s)
    while(end<n):
        if s[end] not in mydic:
            mydic[s[end]] = 1
            uniqueCount +=1

        else:
            mydic[s[end]] +=1
        
        ans = max(ans,uniqueCount)
        while((end - start +1 )>uniqueCount):  #length of string is greater than unique char in string means reapeted ele are there
            
            mydic[s[start]] -=1
            if(mydic[s[start]] == 0):
                uniqueCount -=1
                mydic.pop(s[start])
            start+=1
        
        end +=1
    return ans

s ="pwwkew"

print(lengthOfLongestSubstring(s))