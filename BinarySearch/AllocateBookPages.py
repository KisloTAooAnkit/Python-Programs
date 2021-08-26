def isValid(arr,targetPages,childrenAvailable,n):
    requiredStudents=1
    sln = 0
    for i in range(n):
        if(arr[i]>targetPages):
            return False
        if(sln + arr[i]>targetPages):
            requiredStudents +=1
            sln = arr[i]
        else:
            sln += arr[i]
        if requiredStudents>childrenAvailable:
            return False
    return True




def findPages(arr,childrenCount):
    n = len(arr)
    start = 0
    end = sum(arr)
    ans = 0
    if(n<childrenCount):
        return -1
    while(start<=end):
        mid =  start + (end-start)//2
        if(isValid(arr,mid,childrenCount,n)):
            ans = mid
            end = mid-1
        else:
            start = mid +1
    return ans

arr = [1,2,3,1,1]
m = 4
print(findPages(arr,m))

            

