#https://www.spoj.com/problems/AGGRCOW/
def checkDistanceIfPossible(arr,mid,c,n):
    prevDist =0
    for i in range(n):
        if(arr[i]>=prevDist):
            prevDist = arr[i] + mid
            c-=1
    
    return c<=0
    


def aggrCows(n,c,arr):
    end = max(arr) + 1
    start = 0
    ans = 0
    arr.sort()
    while(start<=end):
        mid = start + (end-start)//2
        test =  checkDistanceIfPossible(arr,mid,c,n)
        if(test):
            ans = mid
            start = mid+1
        elif(not test):
            end = mid-1
    
    return ans

arr = [0,1,2,3]
c=4
print(aggrCows(len(arr),c,arr))
