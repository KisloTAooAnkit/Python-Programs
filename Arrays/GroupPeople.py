#https://leetcode.com/problems/group-the-people-given-the-group-size-they-belong-to/

def groupThePeople(groupSizes):
    ans =[]
    dic = dict()
    n = len(groupSizes)
    for i in range(n):
        number = groupSizes[i]
        if(number in dic):
            dic[number].append(i)
        else:
            dic[number] = [i]
            
    print(dic)
    
    for key in dic:
        arr =  dic[key]
        res =[]
        count = 0
        for i in range(len(arr)):
            res.append(arr[i])
            count+=1
            if(count == key):
                count =0
                ans.append(res)
                res = []
    
    return ans


ls = [2,1,3,3,3,2]

print(groupThePeople(ls))


    
                        