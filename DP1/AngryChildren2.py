import sys
def angryChildren(k, arr):
    # Write your code here
    n = len(arr)
    windowArrSum = 0
    windowAbsDiffSum = 0
    arr.sort()
    ans = sys.maxsize
    start = 0
    end = 0
    #calcting abs for 1st elment 
    for i in range(k):
        end = i
        windowArrSum += arr[i]
        windowAbsDiffSum += arr[end] - arr[start]
    prev=windowAbsDiffSum
    
    for i in range(1,k):
        prev = prev - (k-i)*(arr[i] - arr[i-1])
        windowAbsDiffSum += prev
    flag = True
    while(end<n):
        if not flag :
            windowArrSum += arr[end]
            windowAbsDiffSum += (end-start+1)*arr[end] - windowArrSum
        while(end-start+1 == k):
            flag = False
            ans = min(windowAbsDiffSum,ans)
            absdif = windowArrSum - k*arr[start]
            windowAbsDiffSum -= absdif
            windowArrSum -= arr[start] 
            start+=1
        end+=1
    return ans



arr = [4504,1520,5857,4094,4157,3902,822,6643,2422,7288,8245,9948,2822,1784,7802,3142,9739,5629,5413,7232]
k=5
print(angryChildren(k,arr))
    