#Magic or Dunder methods in python=These are special methods that we can define in our classe, and when invoked, they give you a powerful way to manipulate objects and their behavior.
#MAgic methods also known as "dunders" from the double underscores surrounding their names.

#1.__init__() method=Its a special method that is automatically invoked when you create a new instance of a class.Its responsible for setting up the object's initial state and is also called as "constructor".
#2.__str__() and __repr__() methods= This both str and repr methods are used to convert an object to a string representation.The repr method is taken by the compiler when no str method is present.
#3.__len__() method= Ued to calculate the length of the object given.
#4.__call__() method=Its used to make an object callable,that you can pass it as a parameter to a function and it will execute when the function is called.
class Employee:
    def __init__(self,name):
        self.name=name
    def __len__(self):
        return len(self.name)
    def __str__(self):
        return(f"The name of the Employee is: {self.name}")
    def __repr__(self):
        return(f"Employee('{self.name})")
    def __call__(self):
        return("hey I am Good!!! What about youu??")
e=Employee("Antara")
#All these methods are magical because while printing them we dont need to use double underscores around them.
print(len(e)) #used to tall the length of the string
print(str(e)) #used to print object as string representation
print(repr(e))
print(e()) #used to call a function