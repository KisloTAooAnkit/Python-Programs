
def findMinOps(arr, n):
    left = 0
    right = n-1
    ans = 0
    leftans = arr[0]
    rightans = arr[n-1]
    while(left<right):
        
        if(leftans == rightans):
            left+=1
            right-=1
            leftans = arr[left]
            rightans = arr[right]
            

        elif(leftans<rightans):
            left+=1
            leftans+=arr[left]
            ans+=1

        elif(leftans>rightans):
            right-=1
            rightans+=arr[right]
            ans+=1

    return ans 


arr= [11, 14, 15, 99]


print(findMinOps(arr,len(arr)))
	