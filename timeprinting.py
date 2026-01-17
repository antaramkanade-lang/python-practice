#print Good morning,afternoon or evening with the help of time
#strftime is a builtin function used to denote hours,min & sec
#using ('%H,%M,%S')
import time
timestamp=time.strftime('%H:%M:%S')
print(timestamp)
timestamp=time.strftime('%H')
print(timestamp)
timestamp=time.strftime('%M')
print(timestamp)
timestamp=time.strftime('%S')
print(timestamp)