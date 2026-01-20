#Hybrid Inheritance in python=Its a combination of multiple inheritance and single inheritance or more than one inheritance in OOPs.its a type of inheritance in which multiple inheritance is used to inherit the properties of multiple base classes into a single derived class, and single inheritance is used to inherit the properties of derived class into a sub-derived class.
class BaseClass:
    pass
class Derived1(BaseClass):
    pass
class Derived2(BaseClass):
    pass
class Derived3(Derived1,Derived2):
    pass
#this was the example of hybrid as it is made up of single and multiple inheritance and we can pass the methods into it.

#Hierarchical Inheritance in python=It is made up in a hierarchical way where it makes a tree like structure of the base class and the derived class.
class BaseClass:
    pass
class D1(BaseClass):
    pass
class D2(BaseClass):
    pass
class D3(D1):
    pass