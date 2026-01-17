# os Module in python = its the built-in library that provides functions for interacting with the operating system.It allows you to perform a wide variety of tasks such as reading, writing file, interacting with the file system and running system commands
#dir()= its the python introspection tool used to show everything that the object has like variables,functions,classes & attributes

import os
if(not os.path.exists("data")):
    os.mkdir("data") #When to use os.mkdir ,Use it only when: You want exactly one folder, You are sure it doesn’t already exist
for i in range(0,100):
    os.mkdir(f"data/Day{i+1}") #this will create 100 folders one by one into a new folder

#Rename the folder:-
for i in range(0,100):
    os.rename(f"data/Day{i+1}", f"data/Tutorial{i+1}") #We can rename it by commenting out everything written above except import os and will rename day to Tutorial ,check the folders

#printing all the folders and the data in it if present
import os
folders=os.listdir("data") #we should have to run only this part of printing folders then only it will run error free
print(folders)
for folder in folders:
    print(folder)
    print(os.listdir(f"data/{folder}"))