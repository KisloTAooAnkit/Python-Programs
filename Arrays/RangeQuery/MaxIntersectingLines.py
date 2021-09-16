def maxIntersections(lines):

    lineMap = dict()
    for line in lines:
        start = line[0]
        end = line[1] + 1
    
        if start in lineMap:
            lineMap[start]+=1
        else: 
            lineMap[start]=1
        if end in lineMap:
            lineMap[end]-=1
        else:
            lineMap[end]=-1
    
    res = 0
    cnt = 0
    for entry in sorted(lineMap.keys()):
        cnt += lineMap[entry]
        res = max(res, cnt)
    
    return res

arr = [[1,2],[1,3],[2,4],[3,4],[4,6],[5,6],[6,7]]

print(maxIntersections(arr))
