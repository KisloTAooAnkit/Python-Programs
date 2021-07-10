def minSetSize(arr):
    n = len(arr)
    k = n//2
   
    hashtable = dict()
    for i in arr:
        if(i in hashtable):
            hashtable[i] +=1
        else:
            hashtable[i] = 1

    hashtable = dict(sorted(hashtable.items(), key=lambda x: x[1],reverse=True))
    ans = 0
    for key in hashtable:
        if(hashtable[key]>=k):
            return 1 + ans
        k = k - hashtable[key]
        ans+=1
    return ans


a = [7,7,7,7,7,7]


print(minSetSize(arr=a))
        
        
    



    
        