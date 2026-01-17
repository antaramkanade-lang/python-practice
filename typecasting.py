#TYPECASTING = its the method of converting one data type into another data type
#python supports wide variety of functions or methods like int(),float(),str(),ord(),hex(),oct(),tuple(),set(),list(),dict() etc for the typecasting in python
a="1"
b="2"
print(int(a)+int(b)) #here the no. are written in quotes as a string so we converted them into integer by adding the functn int there.
#Explicit Typecasting= its the conversion of data types which is done by the programmer or user
str="15"
no=7
str_no=int(str)
sum=no+str_no
print("the value of the sum is:",sum)

#Implicit Typecasting= python does not have same order of data types. It has low level and high level orderings so the low level ordered data type converts into high level ordered data type by the python interpreter itself and not by the user.
a=9.2
print(type(a))
b=7
print(type(b))
c=a+b
print(c)
print(type(c)) #here the ans coverted into float accr to ordering of data types