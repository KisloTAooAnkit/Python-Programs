#https://www.codechef.com/CDMN21C/problems/NODRUGS
# cook your dish here
def solution(n,speeds,drugpower,threshold):
    if(n==1):
        return "Yes"
    mymanpower = speeds[n-1]
    othermaxpower = max(speeds[:n-1])
    if(mymanpower>othermaxpower):
        return "Yes"
    if(mymanpower<othermaxpower and drugpower <0):
        return "No"
    
    if drugpower == 0:
        if mymanpower>othermaxpower:
            return "Yes"
        else:
            return "No"
    
    if threshold == 0:
        if mymanpower>othermaxpower:
            return "Yes"
        else:
            return "No"
        
    mymanpower += (threshold-1)*drugpower
    # while(threshold):
    #     if(threshold-drugpower<0):
    #         break
    #     mymanpower+=drugpower
    #     threshold-=drugpower
    
    if mymanpower>othermaxpower:
        return "Yes"
    else:
        return "No"

test = int(input())
while(test):
    n,drugpower,threshold = list(map(int,input().strip().split()))
    speeds = list(map(int,input().strip().split()))
    print(solution(n,speeds,drugpower,threshold))
    test-=1