#Python Decorators= decorators are powerful and versatile tool that allow you to modify the behavior of functions and methods.It is use to decorate the function.A decorator is a function that takes another function as a argument and returns a new function that modifies the behavior of original function.The new function is reffered as "decorated" function.
def greet(fx):
    def mfx(*args, **kwargs): #this is used to pass arguments *args is use to pass in the form of tuple and **kwargs in the form of dictionary
        print("Good Morning")
        fx(*args, **kwargs)
        print("Thanks for using this function")
    return mfx
@greet
def hello():
    print("Hello World")
def add(a,b):
    print(a+b)

hello()
greet(add)(1,2) #if we want to print this arguments then we have to use *args and **kwargs in def mfx()