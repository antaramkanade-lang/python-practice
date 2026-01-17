#Enumerate function in python=it is the built in function that allows you to loop over a sequence (such as list,tuple or string) and get the index and value in sequence at the same time
#using index without Enumerate function:-
marks=[12,15,34,98,76,9,35]
index=0
for mark in marks:
    print(mark)
    if(index==3):
        print("Awesome Antara!")
    index+=1

# Using Enumerate function:-
marks=[12,15,34,98,76,9,35]
for index,mark in enumerate(marks):
    print(mark)
    if(index==3):
        print("Awesome job")

fruits=["mango","orange","apple","banana"]
for index,fruit in enumerate(fruits):
    print(index,fruit)