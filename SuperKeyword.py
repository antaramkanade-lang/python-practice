#Super Keyword in python=The super() keyword is used to refer to the parent class.Its useful when a class inherits from multiple parent classes and you want to call a method from one of the parent classes.
class ParentClass:
    def parent_method(self):
        print("THis is a parent method 1")
class ChildClass(ParentClass):
    def parent_method(self): #here we have taken another parent method in the child class.
        print("Antara 2")
        super().parent_method() #And this super indicates that we have to print the first made parent method of parent class.
    def child_method(self):
        print("This is a child method 2")
child_object=ChildClass()
child_object.child_method() #It will print the child method.
child_object.parent_method() #It will print the parent method of child class and then the first method of parent class due to use of super keyword.

class Employee:
    def __init__(self,name,id):
        self.name=name
        self.id=id
class Programmer(Employee): #here the Programmer becomes a child class and the Employee becomes a parent class.
    def __init__(self,name,id,lang):
        super().__init__(name,id) #This super keyword is used to reduce the extra work of writing the same self.name and self.id.
        self.lang=lang
antara=Employee("Antara",471) #here are two attributes because there are only 2 used in class Employee.
clary=Programmer("clary",341,"python") #here are 3 attributes because there are 3 used in class programmer.
print(antara.name)
print(antara.id)
print(clary.name)
print(clary.id)
print(clary.lang)