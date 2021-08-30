#https://practice.geeksforgeeks.org/problems/find-pair-given-difference1559/1#
class Solution:

    def binSearch(self,start,end,target,arr):
        while(start<=end):
            mid = start + (end-start)//2
            if(arr[mid] == target):
                return True
            
            if(arr[mid]>target):
                end = mid-1
            else:
                start = mid+1
        return False

    def findPair(self, arr, L,N):
        #code here
        arr.sort()
        for i in range(L):
            target = N + arr[i]
            leftans = self.binSearch(0,i-1,target,arr)
            rightans = self.binSearch(i+1,L-1,target,arr)
            if(rightans or leftans):
                return True
        return False
        