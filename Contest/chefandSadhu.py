#https://www.codechef.com/CDMN21C/problems/THREEQ
def solution(key,response):
    keycount = 0
    for i in key:
        if i == 1:
            keycount +=1
    
    rescount = 0 
    for i in response:
        if i == 1:
            rescount +=1
    if rescount == keycount:
        return "Pass"
    else:
        return "Fail"
    
