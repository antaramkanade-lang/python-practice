#Inheritance in python= When a class derives from another class.The child class will inherit all the public and protected properties and methods from the parent class.In addition it can have its own properties and methods.
#1.Single, 2.Multiple, 3.Multilevel, 4.Hierarchical ,5.Hybrid
class Employee:
    def __init__(self,name,id):
        self.name=name
        self.id=id
    def showDetails(self):
        print(f"The name of the employee: {self.id} of {self.name} ")
class Programmer(Employee): #this will print when we change the name of employee to programmer
    def showLanguage(self): #this showLanguage is a child property means its parent which is above does not have this function
        print("The default language is Python")
class Distributor(Programmer): #so this is also i am able to print because i changed the name of e3 from Programmer to Distributor
    def showMarketing(self):
        print("The goods are making a lots of profit")

e1=Employee("Rohan Das",400)
e1.showDetails()
e2=Programmer("Ram charan das",654)
e2.showDetails()
e2.showLanguage() #this will not give error because we have changed the name of e2 as programmer instead of employee
e3=Distributor("Amir chand das",5647)
e3.showDetails()
e3.showMarketing()