def threeSum(arr):
    res = set()

    neg,pos,zero = [],[],[]
    for num in arr:
        if num > 0:
            pos.append(num)
        if num < 0:
            neg.append(num)
        if num == 0:
            zero.append(num)


    N,P = set(neg),set(pos)

    if zero:
        for num in P:
            if -num in N:
                res.add((-num,0,num))
    
    if len(zero)>=3:
        res.add((0,0,0))

    for i in range(len(neg)):
        for j in range(i+1,len(neg)):
            target = -(neg[i]+neg[j])
            if target in P:
                res.add(tuple(sorted([neg[i],neg[j],target])))
    
    for i in range(len(pos)):
        for j in range(i+1,len(pos)):
            target = -(pos[i]+pos[j])
            if target in N:
                res.add(tuple(sorted([pos[i],pos[j],target])))
    

    return res