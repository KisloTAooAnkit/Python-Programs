import sys
def checkIfPossible(computers,targetTimePerComp,batteries):
    totalBatteryReq = computers*targetTimePerComp
    possibleBatterySum = 0
    for battery in batteries:
        if battery > targetTimePerComp:
            possibleBatterySum += targetTimePerComp
        else:
            possibleBatterySum += battery
        
        #early return
        if possibleBatterySum >= totalBatteryReq:
            return True
    
    return possibleBatterySum >= totalBatteryReq



def maximumRunningTime(n,batteries):
    start = 0
    end = sys.maxsize
    maximumTime = -1
    while(start<=end):
        predictedTimePerPC = (start+end)//2
        
        if checkIfPossible(n,predictedTimePerPC,batteries):
            maximumTime = predictedTimePerPC
            start = predictedTimePerPC+1
        else:
            end = predictedTimePerPC-1
    return maximumTime