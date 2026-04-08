'''
1 for snake
-1 for water
0 for gun
'''

import random
computer = random.choice([1 , -1 , 0])
youstr = input("Enter ur choice")
youDict = { "s" : 1 , "w" : -1 , "g" : 0}
reverseDict = {1 : "Snake" , -1: "Water" , 0: "Gun"}
you = youDict[youstr]

print(f"You choose {reverseDict[you]}\nComputer choose {reverseDict[computer]}")

if(computer == you):
    print("It's a Draw!!")
else:
    if(computer== -1 and you == 1):
        print("You win!!")
    elif(computer == -1  and you == 0 ):
        print("You lose!!")
    elif(computer == 1  and you == -1 ):
        print("You lose!!")
    elif(computer == 1  and you == 0 ):
        print("You win!!")
    elif(computer == 0   and you == 1 ):
        print("You lose!!")
    elif(computer == 0  and you == -1):
        print("You win!!")
    else:
        print("Something went wrong!!")


# if((computer - you) == -1  or (computer - you) == 2):
#     print("You lose!!")
# else:
#     print("You win!!")