#Constructors= its a special method in a class which is used to create and initialize the object of a class.Constructor is invoked automatically when the object of class is created. Its main purpose is to initialize or assign values of the data members of that class. it cannot return any value other than None
class person:
    def __init__(self,name,occ):  #this __init__ is a constructor which is used to execute the data of a b and c without printing it separately
        print("Hey I am a person!!")
        self.name=name
        self.occ=occ
    def info(self):
        print(f"Hii my name is {self.name} and I am a {self.occ} !!!")
a=person("Antara","Software Engineer")
b=person("carla","Accountant")
c=person("Tom","Pilot")
a.info()
b.info()
c.info()

#Types of Constructors=
#1.Parameterized constructor= it accepts arguments along with self like def __init__(self,name,occ): . It can be used inside the class to assign the values of data members
#2.Default constructor= it does not accepts any arguments from the object and has only one that is self like def __init__(self): .