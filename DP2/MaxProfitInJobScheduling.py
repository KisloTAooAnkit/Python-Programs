from typing import NamedTuple


class Job:
    def __init__(self,start,end,profit) -> None:
        self.start = start
        self.end = end
        self.profit = profit
    
    def __lt__(self,other):
        return self.start<other.start

def customBinSearch(arr,start,end,time):
    idx = -1
    n = end
    while(start<end):
        mid = start - (end-start)//2
        if arr[mid].start >= time:
            idx = mid
            end = mid-1
        else:
            start = mid+1
    return n if idx == -1 else idx
    

def helper(arr,idx,n,time,length):
    if n<=0:
        return 0
    
    i = customBinSearch(arr,idx,length,time)
    

def jobSchd(startTime,endTime,profit):
    n = len(startTime)
    jobs = []
    for i in range(n):
        jobs.append(Job(startTime[i],endTime[i],profit[i]))

    jobs.sort()
