import random

ch=["rock","paper","scissors"]
user=input("Enter Rock/Paper/Scissor :")
comp=random.choice(ch)

print("You Chose : ",user)
print("Computer Chose : ",comp)

if user == comp:
    print("It's a Tie !!")
elif user == "rock" and comp == "scissors":
    print("You Won !!")
elif user == "scissors" and comp == "paper":
    print("You Won !!")
elif user == "paper" and comp == "rock":
    print("You Won !!")
else:
    print("Computer Won !!")
