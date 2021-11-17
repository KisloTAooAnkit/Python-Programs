import sys
def angryChildren(k,packets):
    packets.sort()
    mindiff = sys.maxsize
    ansstart = 0
    ansend = 0
    start = 0
    end = start +k-1
    n = len(packets)
    #find the right window
    while(end<n):
        if(packets[end]-packets[start]<mindiff):
            mindiff = packets[end]-packets[start]
            ansstart = start 
            ansend = end
        end+=1
        start+=1
        
    #find the sum of that window
    mindiff = 0
    for i in range(ansstart,ansend+1):
        mindiff += packets[i] - packets[ansstart]
    prev = mindiff
    for i in range(ansstart+1,ansend+1):
        prev = prev - ((packets[i]-packets[i-1])*(ansend - i + 1))
        mindiff+=prev
    return mindiff

arr = [4504,1520,5857,4094,4157,3902,822,6643,2422,7288,8245,9948,2822,1784,7802,3142,9739,5629,5413,7232]
k=5
print(angryChildren(k,arr))
    