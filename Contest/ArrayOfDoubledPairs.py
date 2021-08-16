#https://leetcode.com/explore/challenge/card/august-leetcoding-challenge-2021/614/week-2-august-8th-august-14th/3877/
def solution(arr):
       
    dic = dict()
    for i in arr:
        if i in dic:
            dic[i] +=1
        else:
            dic[i] = 1


    count = len(dic)
    print(count,dic)
    for key in dic:
        if key == 0:
            if dic[key] %2 == 0:
                dic[key] = 0
            else:
                return False
        elif dic[key]>0:
            if 2*key in dic:
                val = min(dic[key],dic[2*key])
                dic[key]-= val
                dic[2*key] -= val


  
    for key in dic:
        if dic[key] == 0:
            count-=1

    return count == 0


arr = [4,-2,-4,2]
print(solution(arr))