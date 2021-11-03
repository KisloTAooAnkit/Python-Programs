

def dfs(ans,id1,id2,id3,id4,first,second,third,fourth,n1,n2,n3,n4,n):
    if id1>=n1 and id2>=n2 and id3>=n3 and id4>=n4:
        return

    arr = []
    count = 0
    if id1 < n1:
        arr.append(first[id1])
        count+=1
    if id2 < n2:
        arr.append(second[id2])
        count+=1
    if id3 < n3:
        arr.append(third[id3])
        count+=1
    if id4 < n4:
        arr.append(fourth[id4])
        count+=1
    if count < n:
        return

    val = "".join(arr)
    print(val)
    ans.append(val)

    dfs(ans,id1+1,id2,id3,id4,first,second,third,fourth,n1,n2,n3,n4,n)
    dfs(ans,id1,id2+1,id3,id4,first,second,third,fourth,n1,n2,n3,n4,n)
    dfs(ans,id1,id2,id3+1,id4,first,second,third,fourth,n1,n2,n3,n4,n)
    dfs(ans,id1,id2,id3,id4+1,first,second,third,fourth,n1,n2,n3,n4,n)

    return

def letterCombinations(digits):
    hashmap = { 
        "2" : "abc",
        "3" : "def",
        "4" : "ghi",
        "5" : "jkl",
        "6" : "mno",
        "7" : "pqrs",
        "8" : "tuv",
        "9" : "wxyz"
    }

    first,second,third,fourth = "","","",""
    count = 0
    for num in digits:
        if count == 0:
            first = hashmap[num]
        if count == 1:
            second = hashmap[num]
        if count == 2:
            third = hashmap[num]
        if count == 3:
            fourth = hashmap[num]
        count+=1
    ans = []
    dfs(ans,0,0,0,0,first,second,third,fourth,len(first),len(second),len(third),len(fourth),len(digits))
    
    print(ans)

digits = "23"
print(letterCombinations(digits))