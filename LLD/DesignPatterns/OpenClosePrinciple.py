from enum import Enum
class Color(Enum):
    Red = 1
    Green = 2
    Blue = 3

class Size(Enum):
    Small = 1
    Medium = 2
    Large = 3


class Product:
    def __init__(self,name,color,size) -> None:
        self.name = name
        self.color = color
        self.size = size

#core funda is suppose tum bade project mein kaam krhe ho pehele se classes ban rkhi hai usme so for adding a new functionality you dont modify prewritten code instead you just inherit those classes and add your own functionality 

class ProductFilter:

    def __init__(self) -> None:
        pass

    #not a good practice to create new functions and modifying class for every new icoming requirement
    def filter_by_color(self,products,color):
        for p in products:
            if p.color == color : yield p

    def filter_by_size(self,products,size):
        for p in products:
            if p.size == size: yield p    
    
    def filter_by_size_AND_color(self,products,size,color):
        for p in products:
            if p.color == color and p.size == size:
                yield p


#Specification In above case filter need to know about what condition it is for filtering out elements but in case of below example i am breaking them into two parts specification and filter 
# 
# role of specification is to check whether item satisfies given criteria 
# role of fileter is to check if the element is valid he dosent need to know how that element is valid and what criteria is required 
# It is handled by specification and all filter does is checks if the element is valid yield that element... in this way we only have one method named "filter" which is generalized instead 100s diffrent type filter method in same class 

#determines whether or not if a single item satisfies the given criteria to be overrrided
class Specification:
    def is_satisfied(self,item):
        pass

class Filter:
    def filter(self,items,spec : Specification):
        pass

#check by color
class ColorSpecification(Specification):

    def __init__(self,color) -> None:
        super().__init__()
        self.color = color
    
    def is_satisfied(self, item):
        return item.color == self.color

#cehck by size
class SizeSpecification(Specification):
    
    def __init__(self,size) -> None:
        super().__init__()
        self.size = size
    
    def is_satisfied(self, item):
        return item.size == self.size


#mutiple conditions
#Item shoudl follow every one in list of specifications
class AndSpecification(Specification):
    def __init__(self,*args) -> None:
        super().__init__()
        self.args = args

    def is_satisfied(self, item):
        for specifications in self.args:
            if not specifications.is_satisfied(item):
                return False
        return True



#filter types not implemented in base class as if logic might change so we wont need to modify base class we can change things here only so if you wanna change filter you dont need to mmodify better filter rather you just inherit filter to a new class and do your own custom thing

class BetterFilter(Filter):
    def filter(self, items, spec: Specification):
        for item in items:
            if spec.is_satisfied(item):
                yield item

print('----------------')
print()

if __name__ == '__main__':
    apple = Product('Apple',Color.Green,Size.Small)
    tree = Product('Tree',Color.Green,Size.Large)
    house = Product('House',Color.Blue,Size.Large)

    products = [apple,tree,house]

    pf = ProductFilter()
    print('Green Products (old) ')
    for p in pf.filter_by_color(products,Color.Green):
        print(f'- {p.name} is green')

    
    bf = BetterFilter()
    print('Green products (new)')
    green = ColorSpecification(Color.Green)
    for p in bf.filter(products,green):
        print(f'- {p.name} is green')

    print("Large Products")
    large = SizeSpecification(Size.Large)
    for p in bf.filter(products,large):
        print(f'- {p.name} is large')

    print('Large Blue items')
    blue = ColorSpecification(Color.Blue)
    large_blue = AndSpecification(large,blue)
    for p in bf.filter(products,large_blue):
        print(f'- {p.name} is large and blue')

print()
print('----------------')