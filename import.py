#How importing works in python= importing in python is the process of loading code from python module to current script. This allows you to use the functions and variables defined in the module in your current script
import math
r=math.floor(4.9876) #floor is use to rounding off the nearest integer & the integer should be less than the no. instead of greater
print(r)
result=math.sqrt(9)
print(result)

#from keyword= this is used to import specific function or variable from a module using from keyword
from math import sqrt,pi
result=math.sqrt(9)*pi
print(result)

#Importing everything using * wildcard it imports everything but it is not recommended to use as it can lead to confusion
from math import *
re=math.sqrt(6)*pi*4
print(re)
#as keyword:-
import math as m #here we have taken math as m
result=m.sqrt(9)*m.pi
print(result)
from math import sqrt as s
re=s(9) #here s means sqrt of 9 from math
print(re)

#dir function= it is the built in function called dir that can be used to view the names of all functions and variables defined in a module 
import math
print(dir(math))
print(math.nan,type(math.nan)) # this is a "nan" functn which is called as not a number and used as a float