def meetingRoom(schedule):
    flag = True
    schedule.sort()

    for i in range(1,len(schedule)):
        prev = schedule[i-1]
        curr = schedule[i]
        if(prev[1]>curr[0]):
            return False
    
    True


arr = [[0,30],[5,10],[15,20]]

print(meetingRoom(arr))
