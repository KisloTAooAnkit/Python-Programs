from sys import prefix



def maxSumRangeQuery(arr,requests):
    mod = 10**9 + 7
    n = len(arr)
    diff = [0]*(n+1)
    for left,right in requests:
        diff[left] +=1
        diff[right+1] -=1
    prev = 0
    for i in range(n+1):
        diff[i] +=prev
        prev = diff[i]
    diff.pop()
    diff.sort(reverse = True)
    arr.sort(reverse = True)
    ans = 0

    for i in range(n):
        ans += arr[i]*diff[i]
    return ans%mod

arr = [1,2,3,4,5,10]
requests = [[0,2],[1,3],[1,1]]
print(maxSumRangeQuery(arr,requests))