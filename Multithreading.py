#Multithreading in python=Its the technique in programming that allows multiple threads of execution to run concurrently within a single process.In python,we can use the threading module to implement multithreading.
#concurrent.futures:-It provides a high-level interface for asynchronously executing callables.The asynchronous execution can be performed with threads,using ThreadPoolExecutor,or separate process,using ProcessPoolExecutor.Both implement same interface,which is defined by the abstract executor class.

import threading
import time
from concurrent.futures import ThreadPoolExecutor #This ThreadPoolExecutor is used if we want to schedule the tasks in the bulk.
def func(seconds): #It indicates some task being done.
    print(f"Sleeping for {seconds} seconds")
    time.sleep(seconds)
def main():
 time1=time.perf_counter() #It’s like pressing START on a stopwatch so you can later check how much time passed.
 func(4) #It will print after 4 sec.
 func(2) #It will print after 2 sec.
 func(1) #It will print after 1 sec.
 time2=time.perf_counter()
 print(time2-time1)

#Same code using Threads:-It prints all the three functions at once without consuming separate time for each one.
 t1=threading.Thread(target=func,args=[4]) #If we print how much time taken by this code using threading then it will show zero seconds.
 t2=threading.Thread(target=func,args=[2])
 t3=threading.Thread(target=func,args=[1])
 t1.start()
 t2.start()
 t3.start()
 t1.join() #this is used to wait till the statement is written fully so it will give the time 4sec instead of zero sec because it takes the slowest time required in total of it.
 t2.join()
 t3.join()
 time3=time.perf_counter()
 print(time3-time2)
def poolingDemo():
   with ThreadPoolExecutor() as executor:
      future1=executor.submit(func,3)
      print(future1.result())
      future2=executor.submit(func,2)
      print(future2.result())
      future3=executor.submit(func,4)
      print(future3.result())
      l=[3,5,1,2] #For this list the functions will execute as sleeping for 3 sec or for 5 sec etc...
      results=executor.map(func,l)
      for result in results:
         print(result)
poolingDemo()

