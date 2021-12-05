def sol(s):
    n = len(s)
    arr = [0]*n
    oneCount = 0
    zeroCount = 0
    zero_one_zero = 0
    one_Zero_One = 0
    for i in range(n-1,-1,-1):
        if s[i] == "1":
            oneCount+=1
            arr[i] = zeroCount 
        if s[i] == "0":
            zeroCount +=1
            arr[i] = oneCount
    oneCount = 0
    zeroCount = 0
    for i in range(n):
        if s[i] == "0":
            one_Zero_One += (oneCount)*arr[i]
            zeroCount +=1
        if s[i] == "1":
            zero_one_zero += (zeroCount)*arr[i]
            oneCount +=1
    return zero_one_zero + one_Zero_One

s = "100101"
ans = sol(s)
print(ans)