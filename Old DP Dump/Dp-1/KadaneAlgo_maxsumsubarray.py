import sys

#kadane's algorithm : har index pe best sum kya rahega woh dekhte hai

#O(n)
def maxSubArraySum(arr,n):
    output = [0]*n
    output[0] = arr[0]
    for i in range(1,n):
        output[i] = max(arr[i],arr[i]+output[i-1])
    
    return max(output)

#O(n) but w/o extra array
def maxSubArraySumOpt(arr,n):
    best_sum = -sys.maxsize
    ans=-sys.maxsize
    for i in range(n):
        best_sum = max(arr[i],arr[i]+best_sum)
        ans = max(ans,best_sum)
    return ans

#return array contributing to max sum
def KadanesReturnArray(arr,n):
    s,e = 0,0
    beg = 0
    best = -sys.maxsize
    currsum = -sys.maxsize
    for i in range(n):
        currsum = arr[i] + currsum
        if(currsum<arr[i]):
            currsum = arr[i]
            beg=i
            
        if(currsum>best):
            best = currsum
            s= beg
            e = i
    return s,e,best

arr =[-2,13,-4,-2,1,5,6]

si,ei,ans= KadanesReturnArray(arr,len(arr))
print("arr : ",arr[si:ei+1]," sum : ",ans)
     