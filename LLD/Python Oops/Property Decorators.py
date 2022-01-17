class Employee:
    def __init__(self,first,last) -> None:
        self.first = first
        self.last = last
    @property    
    def email(self):
        return f'{self.first} {self.last}@email.com'
    @property
    def fullName(self):
        return f'The full name of employee is {self.first} {self.last}'
    
    @fullName.setter
    def fullName(self,name):
        self.first,self.last = name.split('-')
    
    @fullName.deleter
    def fullName(self):
        print("cleaning up the first and last names")
        self.first = None
        self.last = None

emp = Employee('Ankit','Singh')
emp.first = 'Sumit'
print(emp.fullName)
print(emp.email)

emp.fullName = 'Madhu-Singh'
print(emp.fullName)
print(emp.email)
del emp.fullName


class A:
    variable = "Hola"
    
    def __init__(self) -> None:
        self.variable = "A"

class B(A):
    variable = "Hello"

a = A()
b = B()
print(b.variable)