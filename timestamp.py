#Exercise no.2 = Timestamp
import time
t=time.strftime('%H:%M:%S')
hour=int(time.strftime('%H'))
hour=int(input("Enter hour:"))
print(hour)
name=input("Enter the name:")
if(hour>=0 and hour<=12):
    print("Good Morning",name)
elif(hour>=12 and hour<=17):
    print("Good Afternoon",name)
elif(hour>=17 and hour<0):
    print("Good Night",name)