import time
import random
def game(player, r, p, s, choices):
    print("You : ", player)
    if player == 'rock':
        print(r)
    if player == 'paper':
        print(p)
    if player == 'scissors':
        print(s)
    computer = random.choice(choices)
    print("computer : ", computer)
    if computer == "rock":
        print(r)
    if computer == "paper":
        print(p)
    if computer == 'scissors':
        print(s)

    if player == computer:
        print(" * * *  It's a Tie  * * * ")
    elif player == 'rock' and computer == 'paper':
        print("You Lose !")
    elif player == 'paper' and computer == 'rock':
        print(" * * *  You Win !  * * * ")
    elif player == 'paper' and computer == 'scissors':
        print("You Lose !")
    elif player == 'scissors' and computer == 'paper':
        print(" * * *  You Win !  * * * ")
    elif player == 'scissors' and computer == 'rock':
        print("You Lose !")
    elif player == 'rock' and computer == 'scissors':
        print(" * * *  You Win !  * * * ")


r = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

p = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

s = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
choices = ['rock','paper','scissors']
print('WELCOME')
while True:
    player = input('Enter your choice (rock, paper, scissors) : ').lower()
    if player in choices:
        game(player,r,p,s,choices)
        intrest = input("Want to play again (Yes / No) : ").lower()
        while intrest not in ['yes', 'no']:
            intrest = input("Want to play again (Yes / No) : ").lower()
        if intrest == 'yes':
            time.sleep(1)
            print('-----------------------------------'
                  '\n-----------------------------------')
        else:
            break
    else:
        print("Invalid input ! ")
        intrest = input("Want to play again (Yes / No) : ").lower()
        while intrest not in ['yes', 'no']:
            intrest = input("Want to play again (Yes / No) : ").lower()
        if intrest == 'yes':
            time.sleep(1)
            print('-----------------------------------'
                '\n-----------------------------------')
        else:
            break