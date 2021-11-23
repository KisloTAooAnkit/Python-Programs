s = input()
s = s.lstrip("[")
s = s.rstrip("]")
arr = [int(ele) for ele in s.split(",")]
sumx = sum(arr)
avg = sumx/len(arr)
print("Sum is={0}".format(sumx))
print("Average is={0}".format(avg))