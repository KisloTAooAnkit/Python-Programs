def sqrt(N):
    start = 0
    end = N
    while(start<=end):
        mid = start + (end-start)//2
        if(mid**2 == N):
            return mid
        elif(mid**2 >N):
            end = mid -1
        else:
            start = mid+1
        
    return end


print(sqrt(400000))