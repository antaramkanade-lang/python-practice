#Recursive Function= we know that a function can call other functions but its even possible for a function to call itself. These type of constructs are called recursive functions
def factorial(num):
    if(num==0 or num==1):
        return 1
    else:
        return(num*factorial(num-1))
num=7
print("number:",num)
print("factorial:",factorial(num))

#Quick Quiz= write a program to print the Fibonacci sequence
def fib(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fib(n - 1) + fib(n - 2)
        
num = 10  # number of terms

print("Fibonacci sequence:")
for i in range(num):
    print(fib(i), end=" ")