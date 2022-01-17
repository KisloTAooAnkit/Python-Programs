def solve(s,e):
    
    dic = {"".join(sorted(list(i))) : 1 for i in s}
    res = 0
    for word in e:
        word = list(word)
        word.sort()
        for idx,letter in enumerate(word):
            a = word[idx]
            word[idx] = ""
            if "".join(word) in dic:
                res +=1
                break
            word[idx] = a
    return res
    

s = ["ant","act","tack"]
e = ["tack","act","acti"]
print(solve(s,e))