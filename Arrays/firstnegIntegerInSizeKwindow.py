#https://practice.geeksforgeeks.org/problems/first-negative-integer-in-every-window-of-size-k3345/1#
from collections import deque
def printFirstNegativeInteger(arr,k):
    q = deque()
    start = 0
    end =0
    n = len(arr)
    ans = []
    while(end<n):
        
        if(arr[end]<0):
            q.append(arr[end])
        
        if(end -start +1 == k):
            
            if(len(q)==0):
                ans.append(0)
            
            elif(arr[start]!=q[0]):
                ans.append(q[0])
            elif(q[0] == arr[start]):
                ans.append(q[0])
                q.popleft()
            
                
            start+=1
        end+=1    
    return ans
arr = [12, -1, -7, 8, -15, 30, 16, 28]
k = 3

print(printFirstNegativeInteger(arr,k))
    