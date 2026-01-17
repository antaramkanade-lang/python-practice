#Local and Global variables=1.Local= it is defined within the function & is only accessible within the functn.It is created when function is called and destroyed when function returns.
#2.Global=it is defined outside the function and can be accessed within or any function in your code
x=4
print(x)
def hello():
    x=5
    print(f"the local x is:{x}")
    print("hello antara")

print(f"the global x is:{x}")
hello()
print(f"the global x is:{x}")

x=10 #global variable
def my_function():
    y=9 #local variable
    print(y)
my_function()
print(x)
#print(y) #this will cause an error because y is local variable and cannot be accessed from outside the function

#global keyword:-it changes the original global variable by staying into the function
x=19
def welcome():
    global x
    x=7
    y=8
    print(y)
welcome()
print(x) #now here the value of x will come 7 instead of 19 because we have used global x in the function so it will take that only