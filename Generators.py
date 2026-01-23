#Generators in python=This are the special types of functions that allows you to create an iterable sequence of values.A generator function returns a generator object,which can be used to generate the values one-by-one as you iterate over it.
#Generator is a powerful tool for working with large or complex data sets,as they allow you to generate the values on-the-fly rather than having to create and store the entire sequence in memory.
#Creating a Generator=You can create a generator using yield statement in a function.The yield statement returns a value from the generator and suspends the execution of the function until the next value is requested.

def my_generator():
    for i in range(50):
        yield i
gen=my_generator()
print(next(gen))
print(next(gen))
print(next(gen))
#So here in this code i have generated only three times of next(gen) then only 3 values like 0,1,2 will get printed from the range of 5000 because in generator it does not store all the value it just execute when it is called without consuming more memory.

#If we apply this thing then the generator will print all the values:-
for j in gen:
    print(j)