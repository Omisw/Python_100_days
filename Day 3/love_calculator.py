# Day 3 - Fifth exercise.


# Love Calculator

# Instructions

# You are going to write a program that tests the compatibility between two people. We're going to use the super scientific method recommended by BuzzFeed.
# To work out the love score between two people:
# Take both people's names and check for the number of times the letters in the word TRUE occurs. Then check for the number of times the letters in the word LOVE occurs. Then combine these numbers to make a 2 digit number.

# This video gives you more details on this:

# For Love Scores less than 10 or greater than 90, the message should be:
# "Your score is **x**, you go together like coke and mentos."
# For Love Scores between 40 and 50, the message should be:
# "Your score is **y**, you are alright together."
# Otherwise, the message will just be their score. e.g.:
# "Your score is **z**."


# 🚨 Don't change the code below 👇
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

lower_name1 = name1.lower()
lower_name2 = name2.lower()

total_true = str(lower_name1.count("t") + lower_name1.count("r") + lower_name1.count("u") + lower_name1.count("e"))
total_love = str(lower_name2.count("l") + lower_name2.count("o") + lower_name2.count("v") + lower_name2.count("e"))

final_percentage = int(total_true + total_love)

if final_percentage <= 10 or final_percentage >= 90:
  print(f"Your score is {final_percentage}, you go together like coke and mentos.")
elif final_percentage >= 40 and final_percentage <= 50:
  print(f"Your score is {final_percentage}, you are alright together.")
else:
  print(f"Your score is {final_percentage}, you are a 0 to the left fot him or her")