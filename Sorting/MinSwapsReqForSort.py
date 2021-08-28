#https://practice.geeksforgeeks.org/problems/minimum-swaps/1


"""My thoughts : Har element ka pair banalo usko index ke saath phir merge intervals wala logic laga skte hai 
    Pairs ko tum sort karo toh woh har pair ke first index ke basis pe sort hoga
    so elements apne sahi jagah pe aagye ab one by one iterate karo pairs pe agar element ka index uske paired index 
    se match nhi hota toh keh skte woh swap hua hai
    isse minimum isliye milega kyunki jo element pehele array mein sorted pos pe the unko ham choo nhi rhe but this might no work
    in case of repeated elements """
def minSwaps(arr):
    n = len(arr)
    pairarr = []
    for i in range(n):
        pairarr.append([arr[i],i])
    pairarr.sort()
    print(pairarr)
    ans = 0
    i =0
    while(i<n):
        pair = pairarr[i]
        if(pair[1] != i):
            print("before : ",pairarr)
            ans+=1
            pairarr[i],pairarr[pair[1]] = pairarr[pair[1]],pairarr[i]
            i-=1
            print("after : ",pairarr)
        i+=1
    return ans

a = [10, 19, 6, 3, 5,0]
print(minSwaps(a))
