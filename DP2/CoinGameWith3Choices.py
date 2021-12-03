def recur(n,x,y):
    if n== 1:
        return True
    if n== 0:
        return False

    if n<0:
        return False
    
    if not (recur(n-x,x,y) or recur(n-y,x,y) or recur(n-1,x,y)):
        return True
    else:
        return False


def coinGame(n,x,y):
    return recur(n,x,y)


n = 2
x = 3
y = 4
print(coinGame(n,x,y))