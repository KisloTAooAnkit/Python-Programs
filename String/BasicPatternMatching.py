def isMatching(s,p):
    n = len(s)
    m = len(p)

    for i in range(n):
        count = m
        for j in range(m):
            if s[i+j] != p[j]:
                break
            count -=1
        if count == 0:
            return True
    return False


s = "abcdefghikjlm"
b = "jlm"
print(isMatching(s,b))