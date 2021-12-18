
def sol(logs,n):
    stack = []
    ans = [0]*n
    lastExeTime = -1
    for log in logs:
        id,action,time = log.split(":")
        if action == "start":
            if stack:
                ans[-1] += int(time) - lastExeTime
            stack.append([int(id)])
            
    return ans

n = 1
logs = ["0:start:0","0:start:2","0:end:5","0:start:6","0:end:6","0:end:7"]
print(sol(logs,n))