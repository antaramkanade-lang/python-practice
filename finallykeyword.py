#Finally keyword= it is the keyword which is used to always execute the statements weather the error occurs or not
def func1():
    try:
        l=[1,5,6,7]
        i=int(input("enter the index:"))
        print(l[i])
        return 1
    except:
        print("some error occured")
        return 0
    finally:
        print("I am always executed") #so this will execute if error occurs or not
x=func1()
print(x)