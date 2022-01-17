<<<<<<< Updated upstream
#-444444
#+-3333
#   +2222




from pickle import NONE


def solve(str: str) -> int:
    value, state, pos, sign = 0, 0, 0, 1

    if len(str) == 0:
        return 0

    while pos < len(str):
        current_char = str[pos]
        if state == 0:
            if current_char == " ":
                state = 0
            elif current_char == "+" or current_char == "-":
                state = 1
                sign = 1 if current_char == "+" else -1
            elif current_char.isdigit():
                state = 2
                value = value * 10 + int(current_char)
            else:
                return 0
        elif state == 1:
            if current_char.isdigit():
                state = 2
                value = value * 10 + int(current_char)
            else:
                return 0
        elif state == 2:
            if current_char.isdigit():
                state = 2
                value = value * 10 + int(current_char)
            else:
                break
        else:
            return 0
        pos += 1

    value = sign * value
    value = min(value, 2 ** 31 - 1)
    value = max(-(2 ** 31), value)

    return value



s ="+2333-2147483646"
x = -1
print(solve(s))
=======
from typing import Counter


def solve(arr,x):
    arr = [str(i) for i in arr]
    x = str(x)
    n = len(arr)
    if n==1:
        return 0    
    dic  = Counter(arr)
    ans = 0
    m = len(x)
    for i in range(0,m-1):
        left = x[:i+1]
        right = x[i+1:]
        if left == right:
            if right in dic:
                ans+= (dic[right] * (dic[right]-1))
        else:
            if right in dic and left in dic:
                ans += dic[right] * dic[left]
    return ans        

arr = [110,11,11]
x = 11011
print(solve(arr,x))
>>>>>>> Stashed changes
