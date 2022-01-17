class Employee:
    raiseAmount = 1.04
    
    def __init__(self,first,last,pay) -> None:
        self.first = first
        self.last = last
        self.email = first + last + '@email.com'
        self.pay = pay
    
    def fullName(self):
        return f'The full name of employee is {self.first} {self.last}'
    
    def apply_raise(self):
        self.pay = int(self.pay * self.raiseAmount)
    

class Developer(Employee):
    raiseAmount = 2.3 #this will override parent class's raiseAmount if we create developer object FOR THAT Object 
    
    def __init__(self,first,last,pay,prog_Language) -> None:
        super().__init__(first,last,pay)
        self.progLanguage = prog_Language

class Manager(Employee):
    
    def __init__(self, first, last, pay,employees=None) -> None:
        super().__init__(first, last, pay)
        self.employees = [] if employees == None else employees    
    def add_emp(self,emp):
        if emp not in self.employees:
            self.employees.append(emp)
        
    def remove_emp(self,emp):
        if emp in self.employees:
            self.employees.remove(emp)
    
    def print_emps(self):
        for emp in self.employees:
            print('-->',emp.fullName())

dev_1 = Developer('Ankit','Singh',6000,'Python')
dev_2 = Developer('Sumit','Singh',6500,'Swift')

mgr_1 = Manager('Sue','Smith',90000,[dev_1])


#1
# print(dev_1.pay)
# dev_1.apply_raise()
# print(dev_1.pay)

#2
# print(dev_1.email)
# print(dev_1.progLanguage)
# print(dev_1.fullName())

#3
print(mgr_1.email)
mgr_1.print_emps()