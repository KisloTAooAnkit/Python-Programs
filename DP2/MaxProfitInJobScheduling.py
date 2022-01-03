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




class Solution:
    
    def helper(self,arr,idx,n,maxLen,dp):
    
        if n<=0:
            return 0
        
        
        if dp[n] != -1:
            return dp[n]

        
        currJob = arr[idx]
        i = bisect_left(arr,Job(currJob.end,0,0),idx+1,maxLen)
        ans1 = arr[idx].profit + self.helper(arr,i,maxLen-i,maxLen,dp)
        ans2 = self.helper(arr,idx+1,n-1,maxLen,dp)
        dp[n] = max(ans1,ans2)
        return dp[n]
    
    
    def jobScheduling(self, startTime: List[int], endTime: List[int], profit: List[int]) -> int:
        n = len(startTime)
        jobs = []
        for i in range(n):
            jobs.append(Job(startTime[i],endTime[i],profit[i]))

        jobs.sort()
        dp = [-1]*(n+1)
        return self.helper(jobs,0,n,n,dp)