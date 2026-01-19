#Class Methods as Alternative Constructors=In OOPS the "constructors " refer to special type of method that is automatically executed when an object is created by an class.The purpose of a constructor is to initialize the objects attributes allowing an object to be fully functional and ready to use.
#there are times when we want to create an object in a different way or with different initial values,than what is provided by the default constructor.This is where class methods can be used as alternative constructors.

class Employee:
    def __init__(self,name,salary):
        self.name=name
        self.salary=salary
    @classmethod
    def fromStr(cls,string): #using this we can print all the objects named string like e2,e3... without writing this separately for each one
        return cls(string.split("-")[0],int(string.split("-")[1])) #this string.split("-") is used to print the the string written down in e2 and e3 as list is separates the items where "-" is applied.
    
e1=Employee("Antara",1200000) #we can also print like this separately
print(e1.name)
print(e1.salary)

string="john-32000"
e2=Employee.fromStr(string)
print(e2.name)
print(e2.salary)
string="Barbiee-64000"
e3=Employee.fromStr(string)
print(e3.name)
print(e3.salary)


class Rectangle:
    def __init__(self,width,height):
        self.width=width
        self.height=height
    @classmethod
    def square(cls,size):
        return cls(size,size)
rectangle=Rectangle.square(50) #you can create a square rectangle like this.
print(rectangle.width)
print(rectangle.height)