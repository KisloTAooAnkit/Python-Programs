def guessNum(n):
    start = 0
    end = n
    while(start<=end):
        mid = start + (end-start)//2
        res = guess(mid)
        if res == 0:
            return mid
        elif res < 0:
            end = mid-1
        else:
            start = mid+1