import string
digs = string.digits + string.ascii_letters
def int2base(x, base):
    if x < 0:
        sign = -1
    elif x == 0:
        return digs[0]
    else:
        sign = 1

    x *= sign
    digits = []

    while x:
        digits.append(digs[x % base])
        x = x // base

    if sign < 0:
        digits.append('-')

    digits.reverse()

    return ''.join(digits)
def oneDigit(num):
    return ((num >= 0) and
            (num < 10))
 

def isPalUtil(num, dupNum):
     

    if oneDigit(num):
        return (num == (dupNum[0]) % 10)
 

    if not isPalUtil(num //10, dupNum):
        return False
 

    dupNum[0] = dupNum[0] //10

    return (num % 10 == (dupNum[0]) % 10)

def isPal(num):
    if (num < 0):
        num = (-num)
    dupNum = [num] 
 
    return isPalUtil(num, dupNum)

def check(base,n):
    i = 1
    ans = 0
    while(n):
        if isPal(i):
            val = int2base(i,base)
            if val == val[::-1]:
                print(val,i)
                ans += i
                n-=1
        i+=1
            
    return ans
k =2
n = 30
print(check(k,n))