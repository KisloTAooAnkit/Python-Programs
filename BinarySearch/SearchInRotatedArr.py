#https://leetcode.com/problems/search-in-rotated-sorted-array/submissions/

class Solution:
    def binSearch(self,arr,target,start,end):
        while(start<=end):
            mid = start + (end-start)//2
            if(arr[mid] == target):
                return mid
            elif(arr[mid]>target):
                end = mid-1
            else:
                start = mid+1

        return -1

    def findMin(self,arr):
        start = 0
        end = len(arr) -1
        n = end+1
        if n== 1:
            return 0
        while(start<=end):
            if(arr[start]<arr[end]):
                return start

            mid = start + (end-start)//2

            prev = (mid - 1 + n) % n
            nxt = (mid+1) %n

            if(arr[mid]<arr[prev] and arr[mid]<arr[nxt]):
                return mid

            elif(arr[mid]<arr[start]):
                end = mid-1

            elif(arr[mid]>arr[end]):
                start = mid+1

    def search(self,arr,target):
        
        mid = self.findMin(arr)
        start = 0
        end = len(arr) - 1
        leftans = self.binSearch(arr,target,start,mid-1)
        righans = self.binSearch(arr,target,mid,end)
        return max(leftans,righans)