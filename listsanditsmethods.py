#Lists in python=lists are ordered collection of data items, they store multiple items in one variable, and they are mutable(means changable after creation). List is accessed using square brackets only.
#List indexing=it starts with 0 and so on...
marks=[7,3,5,"Antara",True] #there can be diifn data types in one list
print(marks)
print(type(marks))
print(marks[0]) #list indexing is shown
print(marks[1])
print(marks[2])
print(marks[3])
print(marks[4])
print("The value after adding the marks is:",marks[0]+marks[1]+marks[2])
#Negative indexing=easy trick:- count the length of list and then subtract it from the index we want to find or we can start counting from last number by -1,-2,-3...
list=[5,8,6,7]
print(list[-3])
print(list[len(list)-3])

#Check whether an item is present in the list or not
marks1=[3,5,8,9,3,0]
print("The list is:",marks1)
if 5 in marks1:
    print("yes 5 is in marks1")
else:
    print("No")

#Jump Indexing
marks=["Antara",3,67,89,4,"avnish",90,76,19,17]
print(marks)
print(marks[1:9])
print(marks[1:9:3]) #this is called jum index that here we have taken 2 after 1:9 then it jumps on second number everytime and skips middle ones 
#List Comprehension= its used to create new lists using dictionary,tuples,and sets even with string and arrays
lst=[i for i in range(10)]
print(lst)
lst=[i for i in range(10) if i%2==0]
print(lst)

#List Methods in python
l=[45,11,67,8,7,64,0,1,2,4,1,1]
print(l)
l.append(7) #it will add 7 in the last of the list
print(l)
l.sort() #it will sort the list from ascending to descending
print(l)
l.reverse()
print(l)
print(l.index(1)) #it checks whats the indexing of 1 that is 9(means 1 is at 9th place)
print(l.count(1)) #it counts how many times 1 occured in the list
m=l.copy()
m[0]=0 #the whole list will be copied as it is and 0th index will be 0
print(m)
l.insert(1,899) #at 1st index 899 will be placed 
print(l)
m=[900,800,700]
k=l+m #both the lists will bein one list togetherly
print(k)
l.extend(m) #it also means adding both the lists in one list
print(l)