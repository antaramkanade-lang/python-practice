#Access Modifiers or Specifiers=its used to limit the access of class variables and class methods outside of a class while implementing the concepts of inheritance
#1.Public access modifier=can be accessed from outside of the class. All the variables and methods in python are by default public.Any instance variable in a class followed by 'self' keyword is publically accessed
class Student:
    def __init__(self,name,age,rollno):
        self.name=name
        self.age=age
        self.rollno=rollno
    def showDetails(self):
        print(f"The name of the student is: {self.name} her age is: {self.age} and her roll num is: {self.rollno}")
obj=Student("Antara",20,3)
print(obj.name,obj.age,obj.rollno) #it shows we can access the data of the class from outside the class
obj.showDetails()


#2.Private access modifier=cannot be accessed from outside of the class only accessed from inside the class it is indicated using double underscore(__) this is known as "weak internal use indicator".its just like the nametag that dont touch it from outside
#Name Mangling= its a technique used to protect class-private and superclass-private attributes from being overwritten by subclasses.Names of class-private and superclass-private attributes are transformed by addition of single underscore and double underscore
class Employee:
    def __init__(self):
        self.__name="Antara Mohan Kanade" #here double underscore is used to indicate that this is a private class
a=Employee()
#print(a.__name) like this we cant print the data of the private class it will throw error
print(a._Employee__name) #this is name mangling used to access the data from private class indirectly
print(a.__dir__()) #this dir function shows all methods and attributes used above


#3.Protected access modifier=can be accessed inside the class and through the subclass or child class.Its indicated using single underscore.Ex if the method called _my_method can only be accessed using its class and subclass.This single underscore is just a naming convention and does not provide any real protection
class Student:
    def __init__(self):
        self._name1="Antara!!!!"
        self._name2="Coding!!!"
    def _funName(self): #Protected method
        return "Code with Harry"
class Subject(Student): #inherited class
    pass
obj=Student()
obj1=Subject()
print(dir(obj))
#Calling by object of Student class
print(obj._name1)
print(obj._funName())
#Calling by object of Subject class
print(obj1._name2)
print(obj1._funName())