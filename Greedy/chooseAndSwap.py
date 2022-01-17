def solution(s):
    dic = dict()
    n = len(s)
    s = list(s)
    for idx,val in enumerate(s):
        if val not in dic:
            dic[val] = idx
    for i,val in enumerate(s):
        cand = val
        for key in dic:
            if dic[key] > i and key < val:
                cand = min(cand,key)
        if cand != val:
            for j,to in enumerate(s):
                if to == cand:
                    s[j] = val 
                elif to == val:
                    s[j] = cand
                
            return "".join(s)
    return "".join(s)


s = "mnopbca"
print(solution(s))
