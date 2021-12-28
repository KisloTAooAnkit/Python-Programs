def romanToInteger(s):
    romanToNumDIc = {"I":1 , "V":5 , "X":10 , "L":50 , "C":100 , "D":500 , "M":1000}

    lstNumAdded = 0
    num = 0
    n = len(s)
    lstNumAdded = romanToNumDIc[s[n-1]]
    num = romanToNumDIc[s[n-1]]

    for i in range(n-2,-1,-1):
        curNum = romanToNumDIc[s[i]]
        #check if smaller number comes before the previous number cases like IX , IV etc
        if curNum < lstNumAdded:
            #remove last number and the add again by reducing it to og val like X is last number inserted 
            #then I comes so i will pull out X and then add IX which is X-I = 10 -i = 9
            num -= lstNumAdded
            num += lstNumAdded-curNum
        else:
            #in other cases add it simply
            num += curNum
        lstNumAdded = curNum
    return num

s = "LVIII"
print(romanToInteger(s))