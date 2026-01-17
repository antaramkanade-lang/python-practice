# OOPs in python= 1.Procedural Programming 2.Object-Oriented Programming
#The procedure we are following till now is procedural programming
#So now in object oriented programming it uses classes and objects to represent real world concepts and entities.
# A class is a blueprint or template for creating objects. it defines the properties and methods that an object of that class will have.Properties are the data or state of an object, and methods are the actions or behavior that an object can perform.
# An object is an instance of a class and it contains its own data and methods.Ex= if ypu create a class called "person" that has properties such as name and age, and methods such as walk() and speak(). Each instance of a person class has an unique object with its own name and age but they would all have same methods to speak and walk.
#One of the key feature of OOP in python is encapsulation, that means the internal state of an object is hidden and can only be accessed or modified through object's method.This helps to protect the data and prevent it from being modified in unexpected ways.
#Another key feature of OOP in python is inheritance, which allows new classes to be created that inherit the properties and methods of the existing class.That is used for code reuse and easy for creating new classes.
#Polymorphism is also supported in python which means that the object of different class are treated as they were the object of common class.This allows for greater flexibility in the code and work with multiple types of objects.

#Classes and Objects in python=
class Person:
    name="Antara"
    age=20
    occupation="Software Engineer"
    networth=100000
a=Person()
print(a.name,a.age,a.occupation,a.networth)   #this are user defined objects. we as user can create or make changes in it they are not by default.

# or we can also write it in the form of f string
class Person1:
    name="carla"
    occupation="Accountant"
    networth=1000
    def info(self):  #this self parameter is used to call the objects for which the self is called at first Ex= if there a, b and c so the self was called for a then it will print or execute only for a and not b and c.
        print(f"{self.name} is a {self.occupation} and earn {self.networth} as her income")
b=Person1()
b.name="Naina"   #here we  can also make changes using this we have written naina and housewife instead of carla and accountant
b.occupation="Housewife"
b.info()
