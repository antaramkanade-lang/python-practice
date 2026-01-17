#Functions in Python= Function:- Its a block of code that performs a specific task whenever it is called. 2 types:-Built-in functn , User-defined functn
#1. built-in = min(),max(),len(),sum(),type(),range(),dict(),list(),tuple(),set(),print(),etc
#2.User-defined= this are created by the user or programmer
#gmean=(a*b)/(a+b)
def calculateGmean(a,b):
    mean=(a*b)/(a+b)
    print(mean)
a=8
b=9
if(a>b):
    print("First number is greater")
else:
    print("Second number is greater")
calculateGmean(a,b)

c=92
d=67
if(c>d):
    print("First number is greater")
else:
    print("Second number is greater")
calculateGmean(c,d)

#Function Arguments and Return Statement:-There are 4 types of arguments 1.Default aguments,Keyword arguments,Variable length arguments,Required arguments
#1.Default aruguments= in this a=9,b=1 are default values if we don't take any values than the average will take this default values
def average(a=9,b=1):#order of variables matter a after then b
    print("the average is:",(a+b)/2)
average() # if we take here the values of a and b then the compiler will not comsider the default values it will transfer to this taken values
def name(fname,lname="john",kname="whatson"): #so these are the default values if we didint take any other names then this values will be considered
    print("Hello",fname,lname,kname)
name("Allezabeth")

#2.Keyword Arguments= we can provide arguments with key=value. It is defined by parameter names. the order of parameters passed does not matter
def average(a,b): #orders of varaiables doesnt matter
    print("the average is:",(a+b)/2)
average(b=9,a=9)

#3.Required arguments =in this we need to pass the value compulsory in the sequential order 
def average(a,b,c=1):
    print("the average is:",(a+b+c)/2)
average(5,6)

#variable-length arguments=sometimes we need to the pass more arguments than those are defined in the actual function
def average(*numbers):#its tuple (tuple is like list but its fixed)
    sum=0
    for i in numbers:
        sum=sum+i
        print("the average is",sum/len(numbers))
average(9,6,4,2,3,8)

def name(**name):
    print("hello",name["fname"],name["mname"],name["lname"],name["pname"]) #its dictionary(these are key -value pairs)
name(fname="john",mname="shrikanth",lname="antara",pname="avnish")