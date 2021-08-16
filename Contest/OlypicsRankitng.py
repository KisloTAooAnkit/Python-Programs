# cook your dish here
test = int(input())
while(test):
    medals = list(map(int,input().strip().split()))
    if(sum(medals[0:3])>sum(medals[3:])):
        print(1)
    else:
        print(2)
    test-=1