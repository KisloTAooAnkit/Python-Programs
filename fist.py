

def minMoves(string):
    lst = list(string)
    start = 0
    end = 0
    xcount = 0
    ans = 0
    n = len(lst)
    dic = dict()
    lastx = -1
    while(end<n):
        if lst[end] == "X":
            xcount+=1

        
        windowS = end - start +1
        if windowS == 3:
            if lst[start] == "X":
                ans +=1
                for i in range(start,end+1):
                    if lst[i] == "X":
                        xcount -=1
                    lst[i] = "0"

            start +=1
        end +=1
    if xcount>0:
        ans +=1
    return ans


s = "X0X0X0X"
print(minMoves(s))