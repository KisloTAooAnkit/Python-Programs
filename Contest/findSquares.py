class DetectSquares:
    
    def __init__(self):
        self.Checkdic = dict()   
        self.coordDic = dict()

    def checkValidPoint(self,point,pointTocheck):
        if point[0] == pointTocheck[0]:
            return True
        if point[1] == pointTocheck[1]:
            return True
        if abs(pointTocheck[1] - point[1]) == abs(point[0] - pointTocheck[0]):
            return True
        return False
        

    def add(self, point) -> None:
        for keys in self.coordDic:
            if self.checkValidPoint(keys,point):
                if self.Checkdic[keys] == 4:
                    if (point[0],point[1]) not in self.Checkdic:
                        self.Checkdic[(point[0],point[1])] = 2
                        self.coordDic[(point[0],point[1])] = [point,keys]
                elif (point[0],point[1]) not in self.Checkdic:
                    self.coordDic[keys].append((point))
                    self.Checkdic[keys] +=1
        if (point[0],point[1]) not in self.Checkdic:
            self.Checkdic[(point[0],point[1])] = 1
            self.coordDic[(point[0],point[1])] = [point]

        

    def count(self, point) -> int:
        ans = 0
        tup = (point[0],point[1])
        for key in self.coordDic:
            if self.checkValidPoint(key,point):
                
                if self.Checkdic[key] == 3:
                    ans +=1
                    self.Checkdic[key] +=1
                    self.coordDic[key].append(point)

                elif self.Checkdic[key] ==4:
                    ans+=1

                elif self.Checkdic[key] <3 :
                    self.Checkdic[key] +=1
                    self.coordDic[key].append(point)

        if tup not in self.Checkdic:
            self.Checkdic[tup] = 1
            self.coordDic[tup] = [point]
        print(ans)
        return ans


detectSquares = DetectSquares();
detectSquares.add([3, 10]);
detectSquares.add([11, 2]);
detectSquares.add([3, 2]);
detectSquares.count([11, 10]);       
detectSquares.count([14, 8]);  
detectSquares.add([11, 2]);    
detectSquares.count([11, 10])
                          

