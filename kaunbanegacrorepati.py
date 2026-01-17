#create a program for displaying questions for kaun banega crorepati
#Use list data types to store the question and their correct answers
#Display the final amount the person is taking home after playing the game
# KBC Game in Python
title=" * ** ** ** KAUN BANEGA CROREPATI * ** ** ** "
print(title)
print("_ _" * 23)
#list of questions
questions=[
    "1. What is the colour of water?",
    "2. Which animal is the king of jungle?",
    "3. How many days are there in a week?"
    ]
#list of options
options=[
    ["a)Red","b)Blue","c)Colourless","d)puple"],
    ["a)Tiger","b)elephant","c)dog","d)lion"],
    ["a)2","b)7","c)10","d)16"]
    ]
#list of correct options
answers=["c","d","b"]
#prize money for each question
prize_money=[1000,5000,10000]
amount_won=0
#logic of game
for i in range(len(questions)):
    print("\n"+questions[i])
    for opt in options[i]:
        print(opt)
        
        
    user_answer=input("Enter your answer(a/b/c/d):")
    if user_answer==answers[i]:
        amount_won=prize_money[i]
        print("Correct Answer!!!!")
        print("You Won ₹",amount_won)
    else:
        print("Wrong Answer///")
        break
print("\n Game Over")
print("you are taking home ₹",amount_won)