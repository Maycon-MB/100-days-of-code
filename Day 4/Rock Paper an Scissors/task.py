import random

# You are going to build a Rock, Paper, Scissors game. You will need to use what you have learnt about randomisation and Lists to achieve this.

# Demo
# https://appbrewery.github.io/python-day4-demo/

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

options = [rock, paper, scissors]

computer_choice = random.choice(options)

user_option = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors\n"))

print(f"You choose:")

if user_option == 0:
    print(rock)
elif user_option == 1:
    print(paper)
elif user_option == 2:
    print(scissors)
else:
    print("Please choose between the 3 options.")

print(f"Computer chose: {options[computer_choice]}")

if user_option == 0 and computer_choice == options[0]:
    print("Draw!")
elif user_option == 0 and computer_choice == options[1]:
    print("You lose!") 
elif user_option == 0 and computer_choice == options[2]:
    print("You win!")
elif user_option == 1 and computer_choice == options[0]:
    print("You win!")
elif user_option == 1 and computer_choice == options[1]:
    print("Draw!")
elif user_option == 1 and computer_choice == options[2]: 
    print("You lose!")
elif user_option == 2 and computer_choice == options[0]:
    print("You lose!")
elif user_option == 2 and computer_choice == options[1]:
    print("You win!")
elif user_option == 2 and computer_choice == options[2]:
    print("Draw!")






