#Loops= loops are used when we have to execute group of statements a certain number of times
#For loop= for loops used to iterate over a sequence of iterable objects in python. Iterating over a sequance means iterating over strings, lists, tuples, sets and Dictionaries
name="Antara"
for i in name:
    print(i)
    if(i=="t"):
        print("This is something special!")
    
colours=["Red","White","yellow","orange","purple"]
for colour in colours:
    print(colour)
    for i in colour:
        print(i)  

#range()= this function is used when dont want to iterate over a whole sequence we only want to iterate over a particular range or a number
for k in range(5001):
    print(k)
for i in range(5):
    print(i)
for n in range(1,12,3):
    print(n) #last no. is 3 so it will give 1,4,7,10 in o/p

#While loop= It executes the statements while the condition is true as soon as the condition brcomes false it breaks the while loop
i=0
while(i<3):
    print(i)
    i=i+1
    
i=int(input("Enter the no.:"))
while(i<20):
    print(i)
    i=i+1
print("Done with the loop")

#Decreamenting While Loop
count=5
while(count>0):
    print(count)
    count=count-1
else:
    print("I am inside the else block")

#Do-While loop= its the loop which executes atleast once irrespective of conditions