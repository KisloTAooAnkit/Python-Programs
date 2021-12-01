from typing import Counter


from collections import defaultdict

def helper(n,idx,wordCount,wordsRemInString,wordDict):
    if wordsRemInString == 0:
        return True
    
    if n <=0:
        return False
    
    


def WordBreak(s,wordDict):
    newWordDict = Counter(wordDict)
    wordCount = defaultdict(int)
    n = len(s)
    #substrings
    for i in range(n):
        for j in range(i,n):
            wordCount[s[i:j+1]] += 1
    totalUniqueWords = len(wordCount)
    
            