#https://www.hackerearth.com/practice/algorithms/searching/binary-search/practice-problems/algorithm/kth-smallest-number-again-2/discussion/the-problems-are-so--1c7e4d5c/

def binSearch(start,end,target):
    while(start<=end):
        mid = start + (end-start)//2
        if(mid==target):
            return mid
        elif(mid<target):
            start = mid+1
        else:
            end = mid-1
    return -1


def KthSmallestAgain(intervals,target):
    n = len(intervals)
    for i in range(n):
        pair = intervals[i]
        noe = pair[1] - pair[0] + 1
        if(target>noe):
            target -=noe
        else:
            return pair[0] + target-1
    return -1


def mergerIntervals(arr,n):
    arr.sort()
    mergerd =[]
    mergerd.append(arr[0])
    for i in range(1,n):
        prevPair = mergerd[-1]
        currentPair = arr[i]
        if(prevPair[1]>currentPair[1]):
            continue
        elif(prevPair[1]<currentPair[1]):
            if(prevPair[1]>=currentPair[0]):
                mergerd[-1] = [prevPair[0],currentPair[1]]
            else:
                if(currentPair[1]-prevPair[0]==1):
                    mergerd[-1] = [prevPair[0],currentPair[1]]
                else:
                    mergerd.append(currentPair)
    return mergerd



def Start(intervals,karr):
    n = len(intervals)
    intervals = mergerIntervals(intervals,n)

    for target in karr:
        print(KthSmallestAgain(intervals,target))
    

# intervals = [[1,5],[10,15]]
# karr = [1,3,6,9]
# Start(intervals,karr)
test = int(input())
while(test):
    intervals = []
    karr = []
    N,Q = list(map(int,input().strip().split()))
    while(N):
        a,b = list(map(int,input().strip().split()))
        intervals.append([a,b])
        N-=1
    while(Q):

        k = int(input())
        karr.append(k)
        Q-=1

    Start(intervals,karr)
    test-=1
