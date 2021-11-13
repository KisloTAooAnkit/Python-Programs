def binSearch(index,n,arr,lastRideEndTime):
    start = index
    end = n
    ans = -2
    while(start<end):
        mid =  start  + (end - start)//2
        ride = arr[mid]
        if lastRideEndTime<=ride[0]:
            ans = mid
            end = mid -1
        elif(lastRideEndTime > ride[0]):
            start = mid +1
    return ans

def maxTaxiEarnings(n,arr):
    arr.sort()
    n = len(arr)

    def calcMaxProfit(totalProfit,index):
        if index < 0 or index>=n:
            return totalProfit

        currentProfit = arr[index][1] - arr[index][0] + arr[index][2]
        nextValidIndex = binSearch(index+1,n,arr,arr[index][1])
        ans1 = calcMaxProfit(totalProfit + currentProfit,nextValidIndex)
        ans2 = calcMaxProfit(totalProfit,index+1)
        return max(ans1,ans2) 

    ans = calcMaxProfit(0,0)
    return ans

arr = [[2,5,4],[1,5,1]]
print(maxTaxiEarnings(5,arr))




# def maxTaxiEarnings(n,arr):
#     arr.sort()
#     n = len(arr)
#     dp = [-1]*(n+1)

#     def calcMaxProfit(totalProfit,index):
#         if index < 0 or index>=n:
#             return totalProfit

#         if dp[index]>-1:
#             return dp[index]

#         currentProfit = arr[index][1] - arr[index][0] + arr[index][2]
#         nextValidIndex = binSearch(index+1,n,arr,arr[index][1])
#         ans1 = calcMaxProfit(totalProfit + currentProfit,nextValidIndex)
#         ans2 = calcMaxProfit(totalProfit,index+1)
#         dp [index] = max(ans1,ans2)
#         return dp[index]

#     ans = calcMaxProfit(0,0)
#     return ans
