#https://practice.geeksforgeeks.org/problems/count-triplets-with-sum-smaller-than-x5549/1
def countPairs(arr,start,end,target):
    count = 0
    while(start<end):
        if(arr[start]+arr[end]<target):
            count += end-start
            start+=1
        else:
            end-=1
    return count




def countTriplets(arr,n,target):
    arr.sort()
    ans = 0
    for i in range(n-2):
        fixd = arr[i]
        pairTarget = target-fixd
        ans += countPairs(arr,i+1,n-1,pairTarget)
    return ans

arr=[-2, 0, 1, 3]
target=2
print(countTriplets(arr,len(arr),target))