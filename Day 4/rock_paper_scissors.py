# Day 4 - Final challenge.


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
import random
random_number = random.randint(0, 2)

choose = int(input("What do you choose? Type 0 for Rock, 1 for paper or 2 for scissors \n"))

if choose == 0:
  print(f"you choose rock {rock}")
elif choose == 1:
  print(paper)
elif choose == 2:
  print(scissors)
else:
  print("Choose again, Only type 0, 1 or 2")

print("Computer chose: ")

if choose > 2:
  print(" ")
elif random_number == 0:
  print(rock)
elif random_number == 1:
  print(paper)
elif random_number == 2:
  print(scissors)


if choose == random_number:
  print("ties")
elif (choose == 0 and random_number == 2) or (choose == 1 and random_number == 0) or (choose == 2 and random_number == 1): 
  print("you win")
elif (choose == 0 and random_number == 1) or (choose == 1 and random_number == 2) or (choose == 2 and random_number == 0): 
  print("you lose")  