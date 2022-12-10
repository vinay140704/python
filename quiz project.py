#Quiz Game
question={"Is Gautam  Adani the richest person in India.":"Yes",
          "Mac operating System is the most optimise OS in the current scenario .":"Yes",
          "English is the most spoken language in the world.":"No",
          "The first full Touch Screen Mobile Phone was Lauched by Apple":"Yes",
          "Marco Polo was the first explorer to reach the South Pole.":"No",
          "Can we Play High end grapics games or Triple A tittles in mac os.":"No",
          "Mice have more bones than humans.":"Yes",
          "The first product with a bar code was chewing gum.":"Yes",
          "The highest currency in the world is Kuwaiti Dinar.":"Yes",
          "Yo-Yo Honey is the Highest Paid Singer in India.":"Yes"}# Pool of questions
import random
questionlist=[]
while(len(questionlist)!=5): # list of 5 questions
    i=random.choice(list(question.keys())) #Choose Random question from question pool and make a list of it
    if(i not in questionlist):
        questionlist.append(i) # make a list of random qustions
score=0
print("Quiz Game:")
for i in questionlist:
    print("\n"+i)
    a=input("\nEnter Yes or No: ")
    if(a==question[i]):
        print("\nRight answer! +5 points")
        score+=5
    else:
        print("\nWrong answer!")
print("\nTotal Score is :",score)
