def wordPattern(pattern: str, s: str) -> bool:    
    arr = s.split(" ")
    wordToPat = dict()
    patternToWord = dict()
    if len(pattern) != len(arr):
        return False
    for idx,word in enumerate(arr):
        if pattern[idx] not in patternToWord:
            if word in wordToPat:
                return False
            patternToWord[pattern[idx]] = word
            wordToPat[word] = pattern[idx]
        else:
            if patternToWord[pattern[idx]] != word:
                return False
    return True 


pattern = "abba"
s = "dog dog dog dog"
print(wordPattern(pattern,s))