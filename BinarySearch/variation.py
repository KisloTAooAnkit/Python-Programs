def binSearch(arr,start,end,k,selectedElement):
    n = end 
    while(start<=end):
        mid = start + (end-start) // 2
        if (abs(selectedElement-arr[mid])>=k):
            end = mid -1
        elif(abs(selectedElement - arr[mid])<k):
            start = mid+1
    return n - end

def calcVariation(arr,k,n):
    arr.sort()
    ans = 0
    for i in range(n):
        start = i+1 
        end = n-1
        selectedEle = arr[i]
        ans += binSearch(arr,start,end,k,selectedEle)
    return ans

"""SILIDING WINDOW Approach nlogn + n"""

def calcVariationSlidingWindow(arr,k,n):
    start = 0
    end = start
    ans = 0
    arr.sort()
    while (end<n):
        while(abs(arr[start] - arr[end])>=k):
            ans += n- end
            start +=1 
        end +=1
    return ans

arr = [1,3,7,11,13,17]
n = len(arr)
k = 4
print(calcVariation(arr,k,n))
print(calcVariationSlidingWindow(arr,k,n))
        
    
    