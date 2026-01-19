#Static methods in python=these are the methods that belong to a class rather than an instance of a class.They are defined using @staticmethod decorator and do not have access to the instance of a class(i.e self)
#We dont need to use an instance 'self' if we are using static methods
class Math:
    def __init__(self,num):
        self.num=num
    def addtonum(self,n):
        self.num=self.num+n
    @staticmethod #here we used static method so no need of using self in it
    def add(a,b):
        return a+b
a=Math(5)
print(a.num)
a.addtonum(6)
print(a.num)
print(Math.add(7,2)) #instead i can easily call this addition using simple Math instance.