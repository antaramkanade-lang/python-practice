# Snake ,Water, Gun Game:-

import random
choices={
    0:"Snake",
    1:"Water",
    2:"Gun"
}
user=int(input("Enter 0 for snake, 1 for water and 2 for gun: "))
computer=random.randint(0,2) #this is used for detecting any random no. from 0 to 2 including 0 and 2 by the computer
print("your chose:",choices[user])
print("computer chose:",choices[computer])

if user==computer:
    print("Its a Draw")
elif (user==0 and computer==1) or \
     (user==1 and computer==2) or \
     (user==2 and computer==0):
    print("User Wins")
else:
    print("Computer Wins")
