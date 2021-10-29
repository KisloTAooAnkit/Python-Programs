def isPossibleToDistribute(amount,k,arr,n):
    tempk = k
    for i in range(n-1,-1,-1):
        tempk -= arr[i]//amount
        if tempk <=0:
            return True
    return False

def distributeCandies(arr,k,n):
    arr.sort()
    start = arr[0]
    end = arr[n-1]
    ans = 0
    while(start<=end):
        mid = start + (end-start)//2
        if isPossibleToDistribute(mid,k,arr,n):
            ans = mid
            start = mid+1
        else:
            end = mid-1
    return ans

arr = [1,3,4]
k = 9
n = len(arr)
print(distributeCandies(arr,k,n))

# test = int(input())
# while(test):
# 	n,k = list(map(int,input().strip().split()))
# 	arr = list(map(int,input().strip().split()))
# 	print(distributeCandies(arr,k,n))
# 	test-=1