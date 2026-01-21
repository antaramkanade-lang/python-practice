#The Time Module in Python=It provides a set of functions to work with time related operations such as timekeeping,formatting,and time conversions.
#This module is a part of Python Standard Library and is available in all python installations,making it a convenient and essential tool for a wide range of applications.

#time.time()=This function returns the current time as a floating point number, representing a number of seconds since the epoch(i.e the point in time when the time module was initialized), the return value is based on computer's system clock & is affected by time adjustments made by OS,such as daylight saving time.
import time
def usingWhile():
    i=0
    while i<5000:
        i=i+1
        print(i)
def usingFor():
    for i in range(5000):
        print(i)
init=time.time() #it gives the time required in seconds.
usingFor()
t1=time.time()-init
init=time.time()
usingWhile()
print(time.time()-init)
print(t1)

#time.sleep()=This function suspends the execution of the current thread for a specific no. of seconds.This function is used to pause the program for a certain period of time,allowing other parts of program to run,or to synchronize the execution of multiple threads.
print(4)
time.sleep(3) #This paused the program for 3 sec and then after 3 seconds it executed the next line.
print("This line is printed after 3 seconds.")

#time.strftime()=This function formats a time value as a string,based on specific format.This function is particularly useful for formatting dates and times in a human readable format.
t=time.localtime()
formatted_time=time.strftime("%Y-%m-%d %H:%M:%S",t)
print(formatted_time)