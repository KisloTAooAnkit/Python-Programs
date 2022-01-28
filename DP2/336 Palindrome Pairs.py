def solve(words):
    dic = {w:i for i,w in enumerate(words)}
    
    for idx,val in enumerate(words):
        
        if val[::-1] in dic and dic[val[::-1]] != idx:
            return True
        
        for i in range(len(val)):
            left = val[:i]
            right = val[i:]
            
            if left[::-1] == left and right[::-1] in dic:
                return True
            if right[::-1] == right and left[::-1] in dic:
                return True
    return False    

arr= ["geekf", "geeks", "or","keeg", "abc", 
          "bc"]

print(solve(arr))