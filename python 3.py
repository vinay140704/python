import random
i=1
c=0
u=0
while (i<=10):
    list = ['s', 'p','c']
    Computer =random.choice(list)
    User=input("Enter your choice:")
    if  Computer=='s' and User=='c':
        print ("Computer Wins")
        i=i+1
        c=c+1
        continue
    elif Computer=='s' and User=='p':
        print("User Wins")
        i=i+1
        u=u+1
        continue
    elif Computer=='s' and User=='s':
        print("tie")
        continue
    elif Computer == 'p' and User == 'c':
        print("User Wins")
        i = i + 1
        u = u + 1
        continue
    elif Computer == 'p' and User == 's':
        print("Computer Wins")
        i = i+1
        c = c + 1
        continue
    elif Computer == 'p' and User == 'p':
        print("tie")
        continue
    if  Computer=='c' and User=='p':
        print ("Computer Wins")
        i=i+1
        c=c+1
        continue
    elif Computer=='c' and User=='s':
        print("User Wins")
        i=i+1
        u=u+1
        continue
    elif Computer=='c' and User=='c':
        print("tie")
        continue

print ("computer wins %d time"%c)
print ("User wins %d time"%u)
if u > c:
     print("User wins")
elif c > u:
          print("Computer Wins")
else:
    print("Its a tie between user and computer")
