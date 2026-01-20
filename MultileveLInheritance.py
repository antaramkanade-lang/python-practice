#Multilevel Inheritance in python= Its a type of inheritance where a derived class inherits from another derived class.it allows you to build a hierarchy of classes where one class builds upon another,leading to a more specialized class.
#It creates levels of derived class by inheriting another derived class like A->B->C->D etc.
class Animal:
    def __init__(self,name,species):
        self.name=name
        self.species=species
    def show_details(self):
        print(f"Name:{self.name}")
        print(f"Species:{self.species}")
class Dog(Animal):
    def __init__(self,name,breed):
        Animal.__init__(self,name,species="Dog")
        self.breed=breed
    def show_details(self):
        Animal.show_details(self)
        print(f"Breed:{self.breed}")
class GoldenRetriever(Dog):
    def __init__(self,name,color):
        Dog.__init__(self,name,breed="Golden Retriever")
        self.color=color
    def show_details(self):
        Dog.show_details(self)
        print(f"Color: {self.color}")
o=GoldenRetriever("Tommy","Black")
o.show_details()
print(GoldenRetriever.mro())