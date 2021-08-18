#https://leetcode.com/problems/find-smallest-letter-greater-than-target/submissions/
def nextGreatestLetter(arr,target):
    start = 0
    n = len(arr)
    end = n-1
    res = 0
    while(start<=end):
        mid = start + (end-start)//2
        if(arr[mid] == target):
            res = mid
            start = mid+1
        
        elif(ord(arr[mid])>ord(target)):
            end = mid-1
        else:
            start = mid+1


    return arr[start%n]


arr = ["e","e","e","e","e","e","n","n","n","n"]
val = "e"
print(nextGreatestLetter(arr,val))