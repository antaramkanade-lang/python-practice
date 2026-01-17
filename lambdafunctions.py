#lambda functions in python = its a small anonymous function without a name it is defined using a lambda keyword and its syntax is: lambda arguments : expression. It can also include multiple statements 
#lambda functions are used in the situations where small function is required for short period of time.They commonly used as arguments to higher-order functions such as map,filter & reduce

def appl(fx,value): #here without using lambda we have to do many steps for just printing the cube
    return 6+fx(value)
double=lambda x:x*2 # this is how we can do any operation using lambda very easily
cube=lambda x:x*x*x
avg=lambda x,y,z:(x+y+z)/3
print(double(5)) #using lambda
print(cube(5)) #using lambda
print(avg(3,5,10)) #using lambda
print(appl(cube,2)) #this is how without using lambda the work increases