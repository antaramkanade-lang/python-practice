#Multiple Inheritance in python= its a powerful method in OOPs which allows a class to inherit attributes and methods from multiple parent classes.This can be useful in situations where a class needs to inherit functionally from multiple sources.
#Its the inheritance where there are two or more sub classes or parent classes which create one derived class.
class Employee:
    def __init__(self,name):
        self.name=name
    def show(self):
        print(f"The name is : {self.name}")
class Dancer:
    def __init__(self,dance):
        self.dance=dance
    def show(self):
        print(f"The dance is : {self.dance}")
class DancerEmployee(Employee,Dancer): #here the first is Employee so the statement for o.show() will print "The name is Antara" of the class Employee.
    def __init__(self,dance,name):
        self.dance=dance
        self.name=name
o=DancerEmployee("Kathak","Antara")
print(o.name)
print(o.dance)
o.show()
print(DancerEmployee.mro()) #this mro tells us “If two parents define the same method, which one do I use?” .This prints a list of classes, in the precise order Python checks when you call a method on a DancerEmployee object.