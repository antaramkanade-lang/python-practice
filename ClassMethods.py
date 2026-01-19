# Class Methods in python= classes are a way to define custom data types that can store data and define functions that can manipulate that data.one type of function that can defined within a class is called a method.
#A class method is a type of method that is bound to the class and not the instance of the class.Class methods are defined using "@classmethod" decorator followed by a function definition.
#Why to use python class methods=ex= you might want to create a factory method that creates instances of your class in specific way.You could define a class method that creates the instance and returns it to the caller.
class Employee:
    company="Apple"
    def show(self):
        print(f"The name is: {self.name} and the company is: {self.company}")
    @classmethod
    def changeCompany(cls,newCompany): #here by default it takes first argument as an instance self but due to the used decorator class method it will take it as a class.
        cls.company=newCompany #so after printing the last statement it will give the company name as Tesla and not Apple due to use of classmethod.
e1=Employee()
e1.name="Antara"
e1.show()
e1.changeCompany("Tesla")
e1.show()
print(Employee.company)