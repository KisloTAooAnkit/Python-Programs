
class CustomLog:
    
    def __init__(self,log):
        logComponents = log.split()
        self.logHeader = logComponents[0]
        self.logPayload = " ".join(logComponents[1:])
    
    
    def __lt__(self,other):
        if self.logPayload == other.logPayload:
            return self.logHeader < other.logHeader
        return self.logPayload < other.logPayload
    
    def isLogTypeDigit(self):
        return ord("0") <= ord(self.logPayload[0]) <= ord("9")
    
    
    def reformLog(self):
        return self.logHeader + " " + self.logPayload

def reorderLogFiles(logs):
    letterLogs = []
    digitLogs = []
    
    
    
    for log in logs:
        customLog = CustomLog(log)

        if customLog.isLogTypeDigit():
            digitLogs.append(customLog)

        else:
            letterLogs.append(customLog)

    letterLogs.sort()
    ans = []
    for customLog in letterLogs+digitLogs:
        ans.append(customLog.reformLog())
    return ans



t = ["dig1 8 1 5 1","let1 art can","dig2 3 6","let2 own kit dig","let3 art zero"]
#["a1 9 2 3 1","g1 act car","zo4 4 7","ab1 off key dog","a8 act zoo"]

print(reorderLogFiles(t))