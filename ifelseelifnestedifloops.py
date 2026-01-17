#if-else condition, elif,nested if conditions
a=int(input("Enter your age: "))
print("age:",a)
if(a>=18):
    print("you can drive")
else:
    print("you cannot drive")
    
applePrice=int(input("Enter price of apple: "))
buget=int(input("Enter the buget: "))
if(applePrice<=buget):
    print("Alexa,put 1kg apple in the cart")
else:
    print("Alexa,do not put anything into the cart")
    
mobCost=int(input("Enter the price of mobile:"))
buget=int(input("Enter the buget:"))
if(buget-mobCost>=10000):
    print("You can definitely buy the mobile")
elif(buget-mobCost>=5000):
    print("Its ok you can buy mobile")
else:
    print("Do not buy mobile")
    
num=int(input("Enter the value of num:"))
if(num<0):
    print(num,"is negative")
elif(num==0):
    print(num,"is zero")
elif(num==999):
    print(num,"is special")
else:
    print(num,"is positive")
print("I am happy now.!")

num=int(input("Enter the number:"))
if(num<0):
    print("The num is negative")
elif(num>0):
    if(num<10):
        print("The num is between 1 to 10")
    elif(num>10 and num<=20):
        print("The num is between 10 to 20")
    else:
        print("The num is greater than 20")
else:
    print("The num is zero")
#conditional operators >,<,>=,<=,==,!=
print(a>18)
print(a<18)
print(a<=18)
print(a>=18)
print(a==18)
print(a!=18)