def answ(arr):
    onebias =0
    zerobias =0
    ans = 0
    for i in range(len(arr)):
        if(arr[i]==1):
            onebias +=1
        elif(arr[i] == 0):
            zerobias +=1
        
        ans = max(zerobias,onebias)
        print(ans)
    
    return ans

a =[0,0,0,0,0,1,1,1,0,0,0,0,0,0]
a = [1,0,0,1,0]
print(answ(a))

