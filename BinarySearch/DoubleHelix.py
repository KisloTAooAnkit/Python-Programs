# your code goes here
def binsearch(arr,target,start,end):

    if(target<arr[0]):
        return -1
    if(target>arr[-1]):
        return -1
    
    while(start<=end):
        mid = start + (end-start)//2
        if(arr[mid] == target):
            return mid
        if(arr[mid]<target):
            start = mid+1
        else:
            end = mid - 1

    return -1

def doubleHelix(arr1,arr2,m,n):
    if(m==0 or n ==0):
        return max(sum(arr1),sum(arr2))
    ans = 0
    runningSum = 0
    otherArraySum = 0
    lastHelixIndex=n
    for i in range(m-1,-1,-1):
        val = binsearch(arr2,arr1[i],0,lastHelixIndex-1)
        runningSum +=arr1[i]
        if(val !=-1):
            
            otherArraySum = sum(arr2[val:lastHelixIndex])
            #print(arr2[val:lastHelixIndex])
            ans += max(runningSum,otherArraySum)
            lastHelixIndex = val
            runningSum = 0
            otherArraySum=0

    ans +=max(runningSum,sum(arr2[:lastHelixIndex]))   
    return ans


def doubleHelixAlt(arr1,arr2,m,n):
    s1 = 0
    s2 = 0
    ans = 0
    i=0
    j=0
    while(i<m and j <n):
        if(arr1[i]<arr2[j]):
            s1+=arr1[i]
            i+=1
        elif(arr1[i]>arr2[j]):
            s2+=arr2[j]
            j+=1
        elif(arr1[i] == arr2[j]):
            ans += max(s1,s2) + arr1[i]
            s1 = 0
            s2 = 0
            j+=1
            i+=1
    if(i<m):
        s1 +=arr1[i]
    if(j<n):
        s2 +=arr2[j]
    
    ans += max(s1,s2)
    return ans


while(True):
    a = list(map(int,input().strip().split()))
    if(a[0]==0):
        break
    print("hello")
    b = list(map(int,input().strip().split()))
    print(doubleHelixAlt(a[1:],b[1:],len(a)-1,len(b)-1))

    