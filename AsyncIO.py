#AsyncIO in python=Asynchronous I/O or async for short,is a programming pattern that allows for high performance I/O operations in a concurrent and non-blocking manner.In python async programming is achieved through the use of asyncio module and its functions.
#It can also helps us to download images and name them and save them into the device by copying the URL and pasting into the code.

import time
import asyncio
async def function1():
    await asyncio.sleep(1) #await is used to wait the code till the first statement completes and then executes the another one.
    print("function 1")
    return "Antara"
async def function2():
    await asyncio.sleep(1)
    print("function 2")
    return "Alphabets"
async def function3():
    await asyncio.sleep(3)
    print("function 3")
async def main():
    L=await asyncio.gather( #It returns the value of the functions but there is no return value for function 3 so None will print.
        function1(),
        function2(),
        function3(),
    )
    print(L)
asyncio.run(main())
