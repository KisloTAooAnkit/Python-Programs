

def sol(s):
    opening = 0
    closing = 0
    ans = 0
    for i in s:
        if i == "(":
            opening +=1
        if i == ")":
            closing +=1

        if opening == closing:
            ans = max(ans,2*opening)
        
        if closing > opening:
            closing = 0
            opening = 0

    opening,closing = 0,0
    
    for i in s[::-1]:
        if i == "(":
            opening +=1
        if i == ")":
            closing +=1
        
        if opening == closing:
            ans = max(ans,2*opening)

        if closing < opening:
            closing = 0
            opening = 0

    return ans

s = "(()"
print(sol(s))