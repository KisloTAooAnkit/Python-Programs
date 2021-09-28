class Item:

    def __init__(self,price,name) -> None:
        self.price = price
        self.name = name

    def __lt__(self,other)-> bool:
        if self.price != other.price:
            return self.price < other.price
        return self.name < other.name





class Mart:
    
    def __init__(self) -> None:
        self.items = []
        self.itemIdx = -1
    

    def view(self):
        self.itemIdx +=1
        return self.items[self.itemIdx].name

    def insert(self,name,price):
        newItem = Item(price,name)
        self.pushInArr(item=newItem)



    def binSearch(self,item:Item) -> int:
        n = len(self.items)
        if n==0:
            return 0
        start = 0
        end = n-1
        while(start<=end):
            mid = start + (end-start)//2
            if self.items[mid] < item:
                start = mid+1
            else:
                end = mid -1

        return start


    def pushInArr(self,item:Item):
        idx = self.binSearch(item=item)
        self.items.insert(idx,item)


if __name__ == '__main__':
    mart = Mart()
    mart.insert('Milk', 4)
    mart.insert('Coffee', 3)
    print(mart.view())
 

    mart.insert('Pizza', 5)
    mart.insert('Gum', 1)
    print(mart.view())

