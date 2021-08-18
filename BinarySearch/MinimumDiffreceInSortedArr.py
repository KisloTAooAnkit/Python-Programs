
# arr mein se woh element nikalo jissse araga mein target subtrack karun to abs diff minimum ho aur woh diff ko return karo

def minDiff(arr,target):
    start = 0
    n = len(arr)
    end = n-1
    while(start<=end):
        mid = start + (end-start)//2
        if (arr[mid] == target):
            return 0
        if(arr[mid]>target):
            end = mid-1
        else:
            start = mid+1

    return min(abs(arr[start%n]-target),abs(arr[end]-target))

arr = [1,3,3,6,6,8,10,12]
target = 0

print(minDiff(arr,target))
