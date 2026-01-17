#Map, Filter and Reduce functions= these are the built-in functions that allow you to apply a function to a sequence of elements and return a new sequence.These are high order functions as they take other functions as arguments.
#map= The map function applies a function to each element in the sequence and returns a new sequence containing the transformed elements.
def cube(x):
    return x*x*x
print(cube(2)) #this is the method of finding cube or any operation

l=[1,9,6,4,7,8]
newl=list(map(lambda x:x*x*x,l)) #this map function is used to print the cube of each element of the list the def and return function is used and lambda can also be used
print(newl)

#filter= this function is used to filter a sequence of elements based on a given predicate and returns a new sequence containing containing only the elements meant to be predicate
def filter_function(a):
    return a>2
newnewl=list(filter(filter_function,l)) #this is filter function it will print only elements greater than two as mentioned in return
print(newnewl)

#reduce= this function is a high order function that applies a function to a sequence and returns a single value. It is the part of functools module
from functools import reduce #Here using import statement for reduce is most imp without import it will throw an error
numbers=[1,2,7,4,1,4]
sum=reduce(lambda x,y:x+y, numbers) #using lambda function we add each element with the other one and make the list shorter and reduce it to a single element
print(sum)