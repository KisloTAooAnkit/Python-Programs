from bisect import bisect_left,bisect_right
class Job:
    def __init__(self,start,end,profit) -> None:
        self.start = start
        self.end = end
        self.profit = profit    
    
    def __lt__(self,other):
        return self.start < other.start
    def __eq__(self, other) -> bool:
        return self.start == other.start
    

def helper(arr,idx,n,maxLen):
    
    if n<=0:
        return 0
    
    currJob = arr[idx]
    i = bisect_left(arr,Job(currJob.end,0,0),idx+1,maxLen)
    ans1 = arr[idx].profit + helper(arr,i,maxLen-i,maxLen)
    ans2 = helper(arr,idx+1,n-1,maxLen)
    return max(ans1,ans2)

def helperDP(arr,idx,n,maxLen,dp):
    if n <= 0:
        return 0

    if dp[n] != -1:
        return dp[n]
    
    currJob = arr[idx]
    i = bisect_left(arr,Job(currJob.end,0,0),idx+1,maxLen)
    ans1 = arr[idx].profit + helper(arr,i,maxLen-i,maxLen)
    ans2 = helper(arr,idx+1,n-1,maxLen)
    dp[n] = max(ans2,ans1)
    return dp[n]
    
def solution(start,end,profit):
    
    n = len(start)
    jobs = []
    for i in range(n):
        jobs.append(Job(start[i],end[i],profit[i]))
    
    jobs.sort()
    dp = [-1]*(n+1)
    return helper(jobs,0,n,n),helperDP(jobs,0,n,n,dp)

start = [1,1,1]
endTime = [2,3,4]
profit =[5,6,4]

print(solution(start,endTime,profit))