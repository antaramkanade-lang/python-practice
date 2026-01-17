#Tuples=this are the ordered colletion of data types like list but it is immutable(we can't change it) and it is written using commas and closed by parenthesis
tup=(1,4,342,54,89,6,3)
print(type(tup),tup)
print(tup[0])
print(tup[-1])
if 6 in tup:
    print("yes 6 is present in tup")
else:
    print("No")
tup2=tup[1:4]
print(tup2)

#Operations on Tuples
#Manipulating tuples= tuples are immuatable so we cannot change it directly so first we have to convert it in list and then make changes and convert it back to tuple
countries=("russia","america","ukraine","india","bangladesh","london")
temp=list(countries) #convert tuple to list
temp.append("newzeland") #Add item to list
temp.pop(3) #remove item from list
temp[2]="Finland" #replace item in the list
countries=tuple(temp) #convert list back to tuple
print(countries)