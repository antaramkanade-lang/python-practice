# "is" vs "==" in python:-
#"is":- it is used to point out exact location of an object in the memory it prints true only if a and b are immutable that does not change like tuple,integer,string etc
#"==" :- it is used to tell the exact value that is a equal to b or not
a=[1,3,5]
b=[1,3,5]
print(a is b) #this will give false because a and b are lists & we can make changes in it so thats mutable
print(a==b) #this will give true because both are equal

c=4
d=4
print(c is d) #True
print(c==d) #True

g=(1,2)
f=(1,2)
print(g is f) #this will print True because a and b are tuple which are immutable that cannot change
print(g==f) #True

a=None
b=None
print(a is b) #True
print(a is None) #True
print(a==b) #True
