def solution(s):
    a ,count1 =[], 100000
    b ,count2 =[], 100000

    n = len(s)
    balance = 0
    for i in range(n):
        if s[i] == "(":
            balance +=1
        elif s[i] == ")":
            balance -=1
            
        a.append(s[i])

        if balance <0:
            count1 -=1
            a[-1] = ""
    
    balance = 0

    for i in range(n-1,-1,-1):
        if s[i] == ")":
            balance +=1
        elif s[i] == "(":
            balance -=1
            
        b.append(s[i])

        if balance <0:
            count2 -=1
            b[-1] = ""
    
    return "".join(a) if count1 > count2 else "".join(reversed(b))

s =  "a)b(c)d"
print(solution(s))
    