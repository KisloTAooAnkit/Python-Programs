#https://www.codechef.com/SEPT21C/problems/TRAVELPS
def solution(journeys,disTime,SateTime):
    ans = 0
    for i in journeys:
        if i == "0":
            ans += disTime
        else:
            ans +=SateTime
    return ans