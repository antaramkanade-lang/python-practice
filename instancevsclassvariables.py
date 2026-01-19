# Instance vs Class variables= variables can be defined at the class level or an instance level.

class Employee: #this is class variable shared by all the objects unless overridden
    companyName="Apple"
    noOfEmployees=0
    def __init__(self,name): #this is an instance variable belong to specific object and created by self defined inside __init__
        self.name=name
        self.raise_amount=0.02
        Employee.noOfEmployees+=1
    def showDetails(self):
        print(f"The name of the Employee is: {self.name} and the raise amount in {self.noOfEmployees} sized {self.companyName} is {self.raise_amount}")
emp1=Employee("Antara")
emp1.raise_amount=0.5 #here i changed the raise amount from 0.02 to 0.5 for emp1
emp1.companyName="Nestle" #here i changed the name of the company for emp1 from Apple to Nestle
emp1.showDetails()