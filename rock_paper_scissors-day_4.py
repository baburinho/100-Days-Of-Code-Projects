# day 4
# rock paper scissors
# ascii art from wynand1004
import random

rock_paper_scissors = ['rock', 'paper', 'scissors']

rps_machine_choice = random.choice(rock_paper_scissors)
rps_user_choice = input("Rock, paper, or scissors? ")
rps_user_choice = rps_user_choice.lower()

rock ="""
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
"""

paper = """
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
"""

scissors = """
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
"""

if rps_user_choice == rps_machine_choice:
    print('Draw.')
elif rps_user_choice == 'rock':
    if rps_machine_choice == 'paper':
        print(paper)
        print("Paper. You lose.")
    else:
        print(scissors)
        print("Scissors. You win.")
elif rps_user_choice == 'paper':
    if rps_machine_choice == 'scissors':
        print(scissors)
        print("Scissors. You lose.")
    else:
        print(rock)
        print('Rock. You win.')
elif rps_user_choice == 'scissors':
    if rps_machine_choice == 'rock':
        print(rock)
        print('Rock. You lose.')
    else:
        print(paper)
        print('Paper. You win.')