#contains info about static class methods and basic OOPS

class Employee:
    numberOfEmployees = 0
    raiseAmount = 1.04
    
    def __init__(self,first,last,pay) -> None:
        self.first = first
        self.last = last
        self.pay = pay
        Employee.numberOfEmployees +=1
    
    def fullName(self):
        return f'The full name of employee is {self.first} {self.last}'
    
    def apply_raise(self):
        self.pay = int(self.pay * Employee.raiseAmount)
    
    #using class method for constructor overloading
    @classmethod
    def from_string(cls,fullname):
        #takes cls as class refrence 
        first,last,pay = fullname.split('-')
        return cls(first,last,pay)
    @staticmethod
    def hasEmployeesGreaterThan(num):
        return Employee.numberOfEmployees > num
    
emp1 = Employee('Corey','Schafer',50000)
emp2 = Employee('Test','User',60000)
print(emp1.fullName())
print(Employee.fullName(emp1))
print(emp1.raiseAmount) # this one works because object ke paas woh varibale nhi hoga agar toh woh class vairables pe dhundne jayega included inherited classes same happens if you access it like self.raiseAmount inside class

Employee.raiseAmount = 1.05 #this line will affect raise ammount value for all objects and class variable

print(emp1.__dict__)
emp1.raiseAmount = 1.05 #this line is NOT accessing class variable but instead it would create another instance variable named raiseAmount exclusive to that object and from now on it would start referring this instance raiseAmount
print(emp1.__dict__) #u can cehck in name space raise amount is created as new variable

print(Employee.numberOfEmployees)

#constructor overloading using class method
string = "Ankit-Singh-76000"
emp3 = Employee.from_string(string)
print(emp3.fullName())

#Static method
print(Employee.hasEmployeesGreaterThan(2))