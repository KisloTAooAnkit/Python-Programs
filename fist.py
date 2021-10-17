import sys
def solution(students,seats):
    students.sort()
    seats.sort()
    dic = dict()
    for i in seats:
        if i not in dic:
            dic[i] = 1
    ans = 0
    for idx,val in enumerate(students):
        minx = sys.maxsize
        idx = -1
        for key in dic:
            if dic[key]>-1:    
                if abs(val-key) < minx:
                    idx = key
                    minx = abs(val-key)
        
        if idx != -1:
            dic[idx] = -1
            ans += minx
    return ans

sts =[2,2,6,6]
students =[1,3,2,6]

print(solution(students,sts))    