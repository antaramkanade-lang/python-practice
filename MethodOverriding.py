#Method Overriding in Python=Its a powerful method of OOps used to redefine a method in a derived class.The method in a derived class is said to override the method in the base class.
#When you create an instance of the derived class and call the overridden method,the version of the method in the derived class is executed ,rather than the version in the base class.
class Shape:
    def __init__(self,x,y):
        self.x=x
        self.y=y
    def area(self):
        return self.x*self.y
class Circle(Shape):
    def __init__(self,radius):
        self.radius=radius
        super().__init__(radius,radius) #this super() is used to take the inputs for radius.
    def area(self):
        return 3.14*super().area() #this is how we can overrides the function by taking super and area from the above class.
rec=Shape(3,5)
print(rec.area())
c=Circle(5)
print(c.area())