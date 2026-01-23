#Function Caching in Python=Its a technique for improving the performance of a program by storing the results of the function call so that you can reuse the results instead of recomputing them every time the function is called.This can be useful when the function is computationally expensive,or when the inputs to the function are unlikely to change frequently.
#Memoization=To store the result of computation so that it can be subsequently retrieved without repeating the computation.

from functools import lru_cache
import time
@lru_cache(maxsize=None) #Here it tells there is no limitations for maximum size so it is None.
def fx(n):
    time.sleep(5) #It is the sleep time where each printing step will take 5 sec and then print the another statement.
    return n*5
print(fx(20))
print("Done for 20")
print(fx(2))
print("Done for 2")
print(fx(6))
print("Done for 6")

#here for printing this all it will not take 5sec for each one because we used cache in our code so it stored the values earlier so now it just takes the value from the cache and print them instead of recomputing them.
print(fx(20))
print("Done for 20")
print(fx(2))
print("Done for 2")
print(fx(6))
print("Done for 6")