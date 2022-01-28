def solve(target,digitsRemaining):
    if target == 0 and digitsRemaining > 1:
        return -1
        
    #basic check even if we fill all slots with 9 does it cross the number ?
    if 9*digitsRemaining < target:
        return -1

    #take out extra 1 and place it on leftmost later incase by filling right 
    #to left the number becomes zero in between
    target = target -1
    ans = 0
    i = 0

    while(digitsRemaining):

        #if current element is >= 9 we place 9 in that place 
        if target >= 9:
            #basic math to add incoming elements properly
            ans = ans + 9*(10**(i)) # 9*(10^i) + prevNumber = 9prevNum
            #reduce from target
            target -=9

        #in this case the number now going to finish in between and
        # target will be reduced to 0 
        elif target < 9:
            #same logic of basic maths but here we are adding target instead of 9
            ans = ans + target*(10**i) # target*(10^i) + prevNumber
            #if there are still slots left we will push 0 for those slots
            target = 0

        #now we add back the deducted one to left most position
        if digitsRemaining == 1:
            ans += 10**i
        
        #10 ^ i factor to effienctly add incoming elements
        i+=1

        digitsRemaining-=1
    print(ans)


t = 54
k = 6
solve(t,k)
    