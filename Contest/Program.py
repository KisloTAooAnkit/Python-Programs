


def check(S,T):
    ans =0
    dic = {"n" : 0, "p": 0,"e":0,"t":0}
    n = len(S)
    for i in range(n):
        if(S[i] == "0" and T[i]=="0"):
            dic["n"]+=1
        elif(S[i]=="1" and T[i]=="0"):
            dic["p"] +=1
        elif(S[i]=="0" and T[i]=="1"):
            dic["e"] +=1
        elif(S[i]=="1" and T[i]=="1"):
            dic["t"] +=1
    print(dic) 
    val = min(dic["n"],dic["t"])
    dic["n"] -=val
    dic["t"] -=val

    val1 = min(dic["e"],dic["p"])
    dic["p"] -= val1
    dic["e"] -=val1

    val2 = min(dic["e"],dic["t"])
    dic["t"] -= val2
    dic["e"] -=val2

    val3 = min(dic["p"],dic["t"])
    dic["p"] -= val3
    dic["t"] -=val3

    val4 = dic["t"]//2

    ans = val1 + val2 + val3 + val4 + val
    return ans



s = "111111"
t = "111011"
print(check(s,t))

# test = int(input())
# while(test):
#     l = int(input())
#     s = input()
#     t = input()
#     print(check(s,t))
#     test-=1
