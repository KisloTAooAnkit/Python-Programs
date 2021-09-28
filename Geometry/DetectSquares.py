class DetectSquares:
    
    def __init__(self):
        self.coordDic = dict()
        self.points = []
        

    def add(self, point) -> None:
        if tuple(point) not in self.coordDic:
            self.coordDic[tuple(point)] =1
        else:
            self.coordDic[tuple(point)] +=1
        self.points.append(point)
        

        

    def count(self, point) -> int:
        res = 0
        px,py = point
        for x,y in self.points:
            if (px == x and py == y) or (abs(px-x) != abs(py-y)):
                continue
            
            else:
                if (px,y) in self.coordDic and (x,py) in self.coordDic:
                    res += (self.coordDic[(px,y)] * self.coordDic[(x,py)])
        return res