

def isValid(diff,val,low,high):
    a = 0
    for i in range(len(diff)):
        a = diff[i] + val
        if a < low:
            return 0
        if a > high:
            return 1
        val = a
    return 2


def solve(diff,low,high):
    
    leftAns = None
    start = low
    end = high
    while(start<=end):
        mid = (start+end)//2
        r = isValid(diff,mid,low,high)
        if r ==2:
            end = mid-1
            leftAns = mid
        elif r == 1:
            end = mid -1
        else:
            start = mid+1
    rightAns = None
    start = low
    end = high
    while(start<=end):
        mid = (start+end)//2
        r = isValid(diff,mid,low,high)
        if r == 2:
            start = mid+1
            rightAns = mid
        elif r == 1:
            end = mid -1
        else:
            start = mid+1
    if leftAns == None or rightAns == None:
        return 0
    return rightAns - leftAns   + 1

arr =[-36115]
l = 50665
u = 89472

# arr =[4,-7,2]
# l = 3
# u = 6
print(solve(arr,l,u))