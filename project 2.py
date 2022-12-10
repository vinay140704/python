from random import randint
n = randint(0,100)
i=7
a=0
print("you have only 7 chance to guess the number between 1 to 100")
while(i>0):
    print("chances left",i)
    n1 = int(input("enter the guess number:\n"))
    if n1>n:
        print("inputted number is greater ,lower the value")
        i=i-1
        a=a+1
        continue
    elif n1<n:
        print("inputted number is smaller ,increase the value")
        i=i-1
        a = a + 1
        continue
    else:
        print("you won")
        a = a + 1
        print ("Number of guessess it took to win is:",a)
        break
