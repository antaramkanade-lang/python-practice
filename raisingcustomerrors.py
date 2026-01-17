#Raising custom Errors

a=input("Enter any number between 5 and 9:")
if a=="quit":
    print("Program executed")
else:
    a=int(a)
    if a<5 or a>9:
        raise ValueError("The number should be between 5 to 9")

salary=int(input("Enter the amount of salary:"))
if not 2000<salary<5000:
    raise ValueError("Salary is insufficient")