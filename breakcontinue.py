#Break Statement= it works till the break condition and then exits the loop
for i in range(12):
    if(i==10):
        break
    print("5*",i+1,"=",5*(i+1))
print("loop ko chodkar bhaag gaya")

#Continue Statement= it skips the current iteration and moves to the further iteration
for i in range(12):
    if(i==10):
        print("skip the current iteration")
        continue
    print("5*",i+1,"=",5*(i+1))
    
#Do-While loop=In python while True is used instead of using "do"
while True:
    num=int(input("Enter the num:"))
    print("The number is:", num)
    if num<0:
        print("exit the loop")
        break