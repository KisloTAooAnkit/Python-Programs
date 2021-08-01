

#https://leetcode.com/problems/sliding-window-maximum/

'''Solution and Explaination by me '''
#https://leetcode.com/problems/sliding-window-maximum/discuss/1373834/python-queue-based-solution-with-king-and-sons-analogy-for-revision


from collections import deque
def maxSlidingWindow(arr,windowSize):
    heirarchyList = deque()
    start = 0
    end = 0
    ans = []
    n = len(arr)
    while(end<n):
        currentCandidate = arr[end]
        while heirarchyList and arr[heirarchyList[-1]] <= currentCandidate:
            heirarchyList.pop()

        heirarchyList.append(end)

        if(end-start +1 ==windowSize):
            ans.append(arr[heirarchyList[0]])
            if(start == heirarchyList[0]):
                heirarchyList.popleft()
            start+=1
        
        end +=1
    return ans

nums = [-7,-8,7,5,7,1,6,0]
k = 4
print(maxSlidingWindow(nums,k))

