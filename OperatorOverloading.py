#Operator Overloading=Its a feature in python that allows developers to redefine the behavior of mathematical and comparison operators for custom data types.
#We can use standard mathematical operators(+,-,*,/ etc) and comparison operators(>,<,==,etc) in your own classes,just as you would for built-in data types like int,float and str.
#It allows you to create more readable and intuitive code.

class Vector:
    def __init__(self,i,j,k):
        self.i=i
        self.j=j
        self.k=k

    def __str__(self):
        return f"{self.i}i + {self.j}j + {self.k}k"
    def __add__(self,x):
        return Vector(self.i+x.i,self.j+x.j,self.k+x.k) #this will print the addition of v1 and v2.
v1=Vector(3,5,6)
print(v1)
v2=Vector(1,2,9)
print(v2)
print(v1+v2)