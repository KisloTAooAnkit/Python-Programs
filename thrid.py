
from typing import Counter


def solve(s,p):
    dic = Counter(p)
    c = 0
    end = 0
    start = 0
    ans = []
    n = len(s)
    m = len(p)
    while(end < n):
        
        if s[end] in dic:
            dic[s[end]] -=1
            if dic[s[end]] >= 0:
                c +=1    

        while(end-start +1 == m):
            if c == m:
                ans.append(start)
            
            if s[start] in dic:
                dic[s[start]] +=1
                if dic[s[start]] > 0:
                    c -=1
            start +=1
        end +=1
    return ans
s = "abab"
p = "ab"
print(solve(s,p))

