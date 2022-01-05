def solve(mass,arr):
    arr.sort()
    n = len(arr)
    for i in range(n):
        if mass >= arr[i]:
            mass+=arr[i]
        else:
            return False
    return True

mass = 5
asteroids =[4,9,23,4]
print(solve(mass,asteroids))