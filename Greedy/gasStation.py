def gasstation(gas,cost):
    n=len(gas)
    posSum = 0
    idx = -1
    prevSum = 0
    temp = [0]*n
    for i in range(n):
        temp[i] = gas[i] - cost[i]
    
    for i in range(n):
        val = posSum + temp[i]
        if val >= 0 :
            posSum = val
            if idx == -1:
                idx = i
        
        elif val< 0:
            prevSum +=val
            posSum = 0
            idx = -1

    if posSum + prevSum >= 0:
        return idx
    else:
        return -1

fuel = [4,5,2,6,5,3]
dist = [3,2,7,3,2,9]
# fuel = [1,4,3,4,3,10]
# dist = [3,5,6,2,7,2]
print(gasstation(fuel,dist)) 


#O(1) space O(n) TC
def gasstationOpt(gas,cost):
    n=len(gas)
    posSum = 0
    idx = -1
    prevSum = 0
    for i in range(n):
        val = posSum + gas[i] - cost[i]
        if val >= 0 :
            posSum = val
            if idx == -1:
                idx = i
        elif val< 0:
            prevSum +=val
            posSum = 0
            idx = -1

    if posSum + prevSum >= 0:
        return idx
    else:
        return -1