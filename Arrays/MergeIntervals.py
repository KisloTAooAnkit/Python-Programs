#https://leetcode.com/problems/merge-intervals/


def mergeIntervalsSol(arr):
    temp = []
    arr.sort()

    temp.append(arr[0])
    n = len(arr)
    for i in range(1,n):
        prev_pair = arr[i]

        MergeInterval(temp,prev_pair)

    return temp


        

def MergeInterval(temp,curr_pair):
    prev_pair = temp[-1]
    if(prev_pair[1]>=curr_pair[0]):
        if prev_pair[1]>=curr_pair[1]:
            temp[-1] = prev_pair
        else:
            new_pair = [prev_pair[0],curr_pair[1]]
            temp[-1] = new_pair
    
    else:
        temp.append(curr_pair)
    
    
            





arr = [[1,3],[2,6],[8,10],[15,18]]
print(mergeIntervalsSol(arr))
    