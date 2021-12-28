
def integerToRoman(num):
    dic = {1:"I" , 4:"IV" , 5:"V" , 9 : "IX" , 10 : "X" , 40 : "XL" , 50 : "L" , 90 : "XC" , 100 : "C",
            400 : "CD" , 500 : "D" , 900 : "CM" , 1000 : "M"}
    numarr = [1,4,5,9,10,40,50,90,100,400,500,900,1000]
    ans = ""
    for val in reversed(numarr):
        if num//val:
            count = num//val
            ans += (count*dic[val])
            num = num%val
    return ans

n = 578
print(integerToRoman(n))

