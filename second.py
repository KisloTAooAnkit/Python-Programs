def ans(digits):
    ans = set()
    n = len(digits)
    for i in range(n):
        val = 0
        val = digits[i]*100
        for j in range(n):
            if j == i:
                continue
            val1 = digits[j]*10
            for k in range(n):
                if k ==j:
                    continue
                val2 = digits[k]
                newVal = val + val1 + val2
                if newVal%2==0 and newVal>=100:
                    ans.add(newVal)
    l = list(ans)
    l.sort()
    return l
di = [2,1,3,0]
print(ans(di))
