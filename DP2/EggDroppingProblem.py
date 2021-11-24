
def eggDrop(eggs,floors):

    if floors ==0:
        return 0
    if floors == 1:
        return 1
    if eggs ==1:
        return floors
    ans = float("inf")
    for floor in range(1,floors+1):
        anda_phat_gya = eggDrop(eggs-1,floor-1)
        anda_nhi_phata = eggDrop(eggs,floors-floor)
        worstcase_for_this_floor = max(anda_nhi_phata,anda_phat_gya) +1
        ans = min(worstcase_for_this_floor,ans)
    return ans

def helperDP(eggs,totalFloors,dp):
    if totalFloors ==0:
        return 0
    if totalFloors == 1:
        return 1
    if eggs ==1:
        return totalFloors
    if dp[eggs][totalFloors]>-1:
        return dp[eggs][totalFloors]
    ans = float("inf")
    for currentFloor in range(1,totalFloors+1):
        anda_phat_gya = helperDP(eggs-1,currentFloor-1,dp)
        anda_nhi_phata = helperDP(eggs,totalFloors-currentFloor,dp)
        worst_case_of_attempts_for_this_floor = 1+max(anda_nhi_phata,anda_phat_gya)
        ans = min(ans,worst_case_of_attempts_for_this_floor)
    dp[eggs][totalFloors] = ans
    return ans


def helperDPBinSearch(eggs,totalFloors,dp):
    if totalFloors ==0:
        return 0
    if totalFloors == 1:
        return 1
    if eggs ==1:
        return totalFloors
    if dp[eggs][totalFloors]>-1:
        return dp[eggs][totalFloors]
    ans = float("inf")
    
    low = 1 
    high = totalFloors
    while(low<=high):
        mid = low + (high-low)//2
        left = helperDPBinSearch(eggs-1,mid-1,dp)
        right = helperDPBinSearch(eggs,totalFloors-mid,dp)
        worst_case = 1 + (max(left,right))
        if left<right:
            low = mid+1
        else:
            high = mid-1
        ans = min(ans,worst_case)
    dp[eggs][totalFloors] = ans
    return ans
    


def eggDropDP(eggs,totalFloors):
    dp = [[-1 for _ in range(totalFloors)] for _ in range(eggs)]
    return helperDPBinSearch(eggs,totalFloors,dp)