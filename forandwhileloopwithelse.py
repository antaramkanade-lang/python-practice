#using the for and while loops with else
#using for loop
for i in range(5):
    print(i)
else:
    print("Sorry no i") #it will run till the no. 4 as it works till n-1 and then it will execute else statement

#if we add break statement in for loop then the else statement will not execute
for i in range(5):
    print(i)
    if i==4:
        break
else:
    print("Sorry no i")

#using while loop
i=0
while i<7:
    print(i)
    i=i+1
    if i==4:
        break
else:
    print("no while loop") #it will not execute else as the loop stoped or breaked earlier

#for loop with else block and format method
for x in range(5):
    print("iteratrion no. {} in the loop".format(x+1))
else:
    print("else block in loop")
print("out of loop")