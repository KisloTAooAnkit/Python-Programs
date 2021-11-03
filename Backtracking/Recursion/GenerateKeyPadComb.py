def keyPadComb(digit,result,letter_hashmap):
    if len(digit) == 0:
        return 0
    
    ans = keyPadComb(digit[1:],result,letter_hashmap)
    
    # this is last digit hence saare alphabhet is digit ke append kardiya res mein
    if ans == 0:
        for alphabet in letter_hashmap[digit[0]]:
            result.append(alphabet)
        return len(result)
    
    n =  len(letter_hashmap[digit[0]])
    
    #duplicate array elements n-1 times as ek set toh pehele se hai array mein 
    for i in range(n-1):
        for i in range(ans):
            result.append(result[i])
            
    #yeha normal multiplication jaise ek dusre ke saath jodrhe with some index algebra
    for idx,alphabet in enumerate(letter_hashmap[digit[0]]):
        for i in range(ans*idx , (ans*idx)+ans):
            newWord = alphabet + result[i]
            result[i] = newWord
    
    return n*ans

def keyPadPickNoPickTypeApproach(digit,dic,ans,word):
    if len(digit) == 0:
        ans.append(word)
        return
    
    n = len(dic[digit[0]])
    x = dic[digit[0]]
    for i in range(n):
        keyPadPickNoPickTypeApproach(digit[1:],dic,ans,word + x[i])
    return

def caller(digit):
    dic = {
        "2" : "abc",
        "3" : "def",
        "4" : "ghi",
        "5" : "jkl",
        "6" : "mno",
        "7" : "pqrs",
        "8" : "tuv",
        "9" : "wxyz"
    }
    
    ans = []
    keyPadPickNoPickTypeApproach(digit,dic,ans,"")
    print(ans)
    
dig = "23"
caller(dig)