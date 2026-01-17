# File IO in python= python provides several ways to manipulate the files
#Opening the file= before we perform any operation on file, we first open it. Python provides open() functn to open file.
#It takes two arguments:the name of the file and the mode in which the file should be open.The mode can be'r' for reading,'w' for writing &'a' for appending
f=open('myfile.txt','r')
text=f.read()
print(text) #here the data will be printed in the output from the another file which is saved named myfile.txt
f.close()

f=open('yourfile.txt','w')
f.write("Whats the colour of the sky????") #now here i have created another file which was not existing using write()
f.close()

f=open('yourfile.txt','a')
f.write('Hello World!!!') #this is appending i added this text in front of the data saved in the file named yourfile.txt
f.close()

with open('myfile.txt','a') as f:
    f.write("What a wonderful day it is!!!!") #using with function we dont need to close the file it automatically closes if 'with' is used

#Modes in file= 1.read(r):- its used to open the file and for read only or gives error if file doesnt exist
#2.write(w):- it opens file for writing or creates the file if it doesnt exist
#3.appens(a):- it is used for appending only and creates another file if it doesnt exist
#4.create(x):- it is used to create a file and give error if file exists already
#5.text(t):- its used to access text file by naming it 'rt' or 'wt' infront of file name
#6.binary(b):- its used to access binary files(images,pdfs etc) by 'rb' or 'wb'
