#The Walrus Operator in Python=Its a new addition to python 3.8 and allows you to assign a value to a variable within an expression.This is useful when you need to use a value multiple times in a loop,but dont want to repeat a calculation.
#It is represented by ':=', syntax and can be used in a variety of contexts including while loops and if statements.

a=True
print(a:=False) #here it will print False in the o/p due to the walrus operator used though we have a is True in first statement.

#Another Example:-
numbers=[1,2,3,4,5]
while(n:=len(numbers))>0: #The no. which are greater than zero, only they will get print in the o/p.
    print(numbers.pop())

#An example without using Walrus operator:-
foods=list()
while True:
    food=input("What food do you like? :")
    if food=="quit":
        break
    foods.append(food)
#Now the same example using the Walrus Operator:-
foods=list()
while(food:=input("What food do you like? :")) !="quit":
    foods.append(food)