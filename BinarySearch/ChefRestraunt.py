def chefRest(timings,personTime,n):
    high = n-1
    low = 0
    while(low<=high):
        mid = low + (high-low)//2
        
        if timings[mid][0] <= personTime <= timings[mid][1]:
            if timings[mid][0] <= personTime < timings[mid][1]:
                return 0
            elif mid == n-1:
                return -1
            else:
                return timings[mid+1][0] - personTime
        
        elif personTime < timings[mid][0]:
            high = mid-1
        
        elif personTime > timings[mid][1]:
            low = mid+1
    
    if low == n:
        return -1
    else:
        return timings[low][0] - personTime

# a = [[2, 3], [5, 7], [9, 10], [20, 30]]
# p = 1
# print(chefRest(a,p,4))


test = int(input())
while(test):
    
    timeInp,personTims = list(map(int,input().strip().split()))
    n = timeInp
    timings = []
    while(timeInp):
        pair = list(map(int,input().strip().split()))
        timings.append(pair)
        timeInp -=1
    timings.sort()
    while(personTims):
        time = int(input())
        print(chefRest(timings,time,n))
        personTims -=1
    test -=1