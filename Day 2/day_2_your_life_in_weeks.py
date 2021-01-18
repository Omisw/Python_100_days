# Day 2 - Third exercise.

# Your Life in Weeks
# Instructions
# I was reading this article by Tim Urban - Your Life in Weeks and realised just how little time we actually have.

# https://waitbutwhy.com/2014/05/life-weeks.html

# Create a program using maths and f-Strings that tells us how many days, weeks, months we have left if we live until 90 years old.

# 🚨 Don't change the code below 👇
age = input("What is your current age? \n")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

age_int = int(age)
age_left = 90 - age_int

age_days = age_left * 365
age_months = age_left * 12
age_weeks = age_left * 52

print(f"You have {age_days} days, {age_weeks} weeks, and {age_months} months left.")