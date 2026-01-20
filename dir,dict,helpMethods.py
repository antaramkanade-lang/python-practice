# dir(),__dict__() and help() methods in python=They makes it easy for us to understand how classes resolve various functions and execute code.
#In Python there are three built-in functions that are commonly used to get information about objects : dir(),dict,help().

#The dir() method:-This function returns all the attributes and methods(including dunder methods) available for an object.Its an useful tool that discovers what you can do with an object.
x=[1,2,3]
print(dir(x)) #it will give the list of the methods or attributes present in this code or list.
print(x.__add__)#this is one of the methods of it and we will check its o/p by printing it.

#The __dict__() method=its an attribute or method that returns a dictionary representation of an object's attribute.useful for introspection.
class Person:
    def __init__(self,name,age):
        self.name=name
        self.age=age
        self.version=1
p=Person("Antara",20)
print(p.__dict__) #using dict everything written will be executed in the key:value pair as a dictionary.

#The help() method= its used to get help documentation for an object, including a description of its attributes and methods.
print(help(Person)) #here we used Person of the above code so it will tell every thing like documentation of that.