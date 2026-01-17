#Short hand if else statements = writing if else statements in a single line
a=int(input("Enter the value of a:"))
b=int(input("Enter the value of b:"))
print("A") if a>b else print("=") if a==b else print("B")
c=9 if a>b else 0 #this will print if a>b.
print(c)