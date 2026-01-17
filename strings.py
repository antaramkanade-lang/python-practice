# String = its the collection of textual data. Anything written in the single or double quotes is called string 

name="Antara"
friend="Avnish"
print(name+friend)

#use of a string using for loop 
apple='''He said,
How are you?
"I want to eat an apple'''
print(apple)
for character in apple:
    print(character)
    # here we wanted to print each letter seperately in a line so we used for loop because of lots of data in apple string

#string Slicing

fruit="Mango"
lenFruit=len(fruit)
print(lenFruit)
print(fruit[0:5])
print(fruit[1:4])
print(fruit[0:-3]) #it subtracts the -ve no. from the lenght i.e 5-3=2 so the ans will be 'Ma'
print(fruit[:])#it will automatically print the original value of string

#String Methods
#Strings are immutable- it cannot be modified but there are built-in features through which we can modify
a="!!! Antara!! !!!!!!!"
print(len(a))
print(a)
print(a.upper())
print(a.lower())
print(a.rstrip("!")) #it removes the thing written in quotes but only the last ones not the beggining ones
print(a.replace("Antara","John"))
print(a.split(" ")) #it splits the words separately with quotes which have gaps in between them in the original string

blogHeading="introduction tO jS"
print(blogHeading.capitalize()) #it capilizes 1st letter and also arranges other letters properly

str1="Welcome to the Console!!!"
print(len(str1))
print(len(str1.center(50))) #it brings the valus in center
print(a.count("Antara"))
print("@" in a) #this is used to check wether that particular letter,word or symbol is present in the string or not using true or false