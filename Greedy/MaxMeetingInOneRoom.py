def maxMeetingsInOneRoom(arr,dep):
    n = len(arr)
    meetings = [(arr[i],dep[i],i) for i in range(n)]
    meetings.sort(key=lambda x : x[1])
    lastMeetingEndTime = -1
    ans = []
    for i in range(n):
        start = meetings[i][0]
        end = meetings[i][1]
        idx = meetings[i][2]
        if start > lastMeetingEndTime:
            ans.append(idx+1)
            lastMeetingEndTime = end
    return ans


s ,f= [75250, 50074, 43659, 8931, 11273, 27545, 50879, 77924], [112960, 114515, 81825, 93424, 54316, 35533, 73383, 160252]
print(maxMeetingsInOneRoom(s,f))