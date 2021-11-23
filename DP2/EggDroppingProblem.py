
def helper(eggs,floors):
    if eggs ==1:
        return floors
    if floors ==0:
        return 0
    if floors == 1:
        return 1
    ans = 0
    for floor in range(floors+1):
        anda_phat_gya = helper(eggs-1,floors-1)
        anda_nhi_phata = helper(eggs,floors-floor)
        worstcase_for_this_floor = max(anda_nhi_phata,anda_phat_gya) +1
        ans = min(worstcase_for_this_floor,ans)
    return ans

def eggDrop(eggs,floors):
    if eggs ==1:
        return floors
    if floors ==0:
        return 0
    if floors == 1:
        return 1
    ans = 0
    for floor in range(floors+1):
        anda_phat_gya = helper(eggs-1,floors-1)
        anda_nhi_phata = helper(eggs,floors-floor)
        worstcase_for_this_floor = max(anda_nhi_phata,anda_phat_gya) +1
        ans = min(worstcase_for_this_floor,ans)
    return ans