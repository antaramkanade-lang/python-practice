#Match-Case Statement= it is a switch-case statement and very similar to if-else statement
x=int(input("Enter the number x:"))
match x:
    #if x is 0
    case 0:
        print("The value of x is zero")
    case 4:
        print("The value of x is four")
    case _ if x!=90:
        print("The value is not 90")
    case _ if x!=80:
        print("The value is not 80")
    case _:
        print(x)