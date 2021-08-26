#https://leetcode.com/problems/capacity-to-ship-packages-within-d-days/




def isShipCapable(arr,currwght,totaldays,n):
    requiredDays = 1
    runningWeight = 0
    for i in range(n):
        if(arr[i]>currwght):
           return False
        if(runningWeight+arr[i]>currwght):
            requiredDays +=1
            runningWeight = arr[i]
        else:
            runningWeight += arr[i]
        if(requiredDays>totaldays):
            return False
    return True

def shipWithinDays(arr,days):
    start = 0
    end = sum(arr)
    n =len(arr)
    ans = 0
    while(start<=end):
        mid = start + (end-start)//2
        if(isShipCapable(arr,mid,days,n)):
            ans = mid
            end = mid -1
        else:
            start = mid+1

    return ans

a = [1,2,3,1,1]
d = 4
print(shipWithinDays(a,d))
