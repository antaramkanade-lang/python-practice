#Set methods:-1.Union() and update()
cities1={"tokyo","india","london","america"}
cities2={"tokyo","paris","switzerland","india"}
cities3=cities1.union(cities2) #it adds both the sets togetherly in one set
print(cities3)
print(cities1.update(cities2)) #it checks whats left in the one set that is present in the another one and add that values to the set

# 2.intersection() and intersection_update():
c1={"anil","antara","avnish","laxmi"}
c2={"aparna","mohan","avnish","antara"}
c3=c2.intersection(c1) #it checks the common values betw 2 sets and print them
print(c3)
c1.intersection_update(c2) #it only gives the common values and ignore all the other value and update methods are written in diifn way
print(c1)

#3.symmetric_difference() and symmetric_difference_update():
set1={"dog","cat","elephant","wolf"}
set2={"giraffe","dog","cat","rhino"}
set3=set2.symmetric_difference(set1) #it only prints the uncommon values and ignore the common ones
print(set3)

#4.difference() and difference_update():
set=set2.difference(set1) #it printed that values of set2 which are not present in set1
print(set)

#set methods= there are various built-in methods used for the manipulation of sets
#1.isdisjoint()=it checks if there are common values in two sets then it returns false otherwise true
print(set2.isdisjoint(set1))
#2.issuperset()=it checks if one set is the subset of another set or not means are the values of set2 orginally present in set1 or not
print(set2.issuperset(set1))
#3.issubset()=its the opposite of superset it checks it the values of original set is present in the particular set
print(set2.issubset(set1))
#4. add()=it is used to add only single item in the set
se1={"pizza","momos","colddrink"}
se1.add("chocolate")
print(se1)
#5.update()=it is use to add more than one items in the set
se2={"tea","coffee","milk","ice"}
se1.update(se2)
print(se1)
#5.remove()/discard()=used to remove an item from set. if we remove the item which is not present in set then remove will throw error but discard will not
se1.remove("pizza")
print(se1)
#6.pop()=it basically removes the last item but as sets are unordered so we dont know which item it will pop
item=se1.pop()
print(se1)
print(item)
#7.del=its used delete an entire set and in o/p it gives as set not defined
# del set1
print(set1)
#8.clear()= its used when we dont want to dlt entire set and just dlt all the elements in it and return an empty set
set2.clear()
print(set2)
#9.check if item is present in set:
info={"carla",19,True,"dog"}
if "carla" in info:
    print("carla is present in info")
else:
    print("not pesent")