import random


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

user_choice = input("press 1 for rock, 2 for the paper , 3 for scissors")

computer_choice = random.randint(0,2)
print(f"computer chose {computer_choice}")
 

