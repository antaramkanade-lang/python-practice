#Single Inheritance=its a type where a class inherits properties and behaviors from a single parent class.This is simplest and common form of inheritance.
#There is one child class or sub class that inherits from one parent class or super class.

class Animal:
    def __init__(self,name,species):
        self.name=name
        self.species=species
    def make_sound(self):
        print("Sound made by an animal")
class Dog(Animal):
    def __init__(self,name,breed):
        Animal.__init__(self,name,species="Dog")
        self.breed=breed
    def make_sound(self):
        print("Bark!")
d=Dog("Dog","Doggerman")
d.make_sound()
a=Animal("Dog","Dog")
a.make_sound()

#Quick Quiz=Implement a Cat class by using the animal class.Add some methods specific to class.
class Animal:
    def __init__(self,name,species):
        self.name=name
        self.species=species
    def make_sound(self):
        print("Sound made by an animal")
class Cat(Animal):
    def __init__(self,name,breed):
        self.breed=breed
        super().__init__(self,name)
    def make_sound(self):
        print("Meowww!!!")
c=Cat("Cat","Pusycat")
c.make_sound()
a=Animal("Cat","Cutieecat")
a.make_sound()