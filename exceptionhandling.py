#Exception handling= its the process of handling unexpected or unwanted events in program. It handles errors
a=int(input("Enter the no.:"))
print(f"The multiplication of {a} is:")
for i in range(1,11):
    print(f"{int(a)} x {int(i)} = {int(a*i)}")
print("End of the code")

#use of try and except when error occurs
x=input("Enter the number:")  #now here instead of any no. i take a string in the output
print(f"the number {x} is an integer")
try:
    for i in range(1,11): #if we take a string then this loop will not run but using try it will allow the further lines to run
        print(f"{int(x)} x {int(i)} = {int(x*i)}")
except:
    print("Invalid Input") #here except is use to show the error and run the further lines in the output
print("Some imp lines of code")
print("End of the code")

#we can handle ValueError also if we have taken int(input()) in the code and then taken the string instead of integer then how to handle it
try:
    num=int(input("Enter the value of num:"))
    a=[6,3]
    print(a[num])
except ValueError:
    print("Number entered is not an integer")
except IndexError:
    print("Index Error") #this error will occur if put an greater integer like 4 out of the capacity of list of a as it has index 0 and 1 only.