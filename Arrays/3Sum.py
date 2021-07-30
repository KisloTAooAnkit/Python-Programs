def threeSum(arr):
    ans =[]
    arr.sort()
    n = len(arr)
    print(arr)
    if(n<3):
        print("ghusa")
        return ans

    if(n==3):
        if sum(arr) ==0 :
            ans.append(arr)
            return ans
        

    for i in range(0,n-3):

        if(i>0 and arr[i-1]==arr[i]):
            continue
        a = arr[i]
        start = i+1
        end = n-1
        print(start,end)
        while(start<end):


            b = arr[start]
            c = arr[end]
            val = a+b+c
  
            if(val==0):
                ans.append([a,b,c])
                while(arr[start]==arr[start+1]):
                    print(start)
                    start+=1
            elif(val<0):
                while(arr[start]==arr[start+1]):
                    print(start)
                    start+=1
                
            elif(val>0):
                while(arr[end]==arr[end-1]):
                    print(end)
                    end-=1
                

    return ans
arr =[-1,0,1,2,-1,-4]

print(threeSum(arr))
