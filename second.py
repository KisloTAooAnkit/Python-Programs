<<<<<<< Updated upstream
def solve(arr):
    i = 0
    ans = 0
    n = len(arr)
    while(i<n):
        peak = i
        start = i
        while(i+1<n and arr[i] < arr[i+1]):
            i+=1

        haveWeClimbedAnyStep = start < i

        if haveWeClimbedAnyStep:
            peak = i
        else:
            i+=1
            continue
        
        while(i+1<n and arr[i]>arr[i+1]):
            i+=1
        
        haveWeGotDownAnyStep = i > peak

        if haveWeGotDownAnyStep:
            end = i
        else:
            i+=1
            continue
        
        ans = max(ans,end-start+1)

        

=======
>>>>>>> Stashed changes
