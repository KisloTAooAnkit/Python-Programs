def solution(a,b,c,d,e):
    sm = a+b+c
    p1 = a+b
    p2 = a+c
    p3 = b+c


    if(p1<=d and sm-p1<= e):
        return "YES"

    if(p2<=d and sm-p2<= e):
        return "YES"

    if(p3<=d and sm-p3<= e):
        return "YES"

    return "NO"