def findingUsersActiveMinutes(logs, k):
    logs.sort()
    hashtable = dict()
    answer = [0]*k
    for i in logs:
        id = i[0]
        time = i[1]
        if(id in hashtable):
            hashtable[i] +=1
        else:
            hashtable[i] =1
            
    for key in hashtable:
        val = hashtable[key]
        answer[val-1] +=1
    return answer


logs = [[0,5],[1,2],[0,2],[0,5],[1,3]]
k = 5

print(findingUsersActiveMinutes(logs,k))
