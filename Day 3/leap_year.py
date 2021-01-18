# Day 3 - Third exercise.


# Leap Year

# Instructions
# Write a program that works out whether if a given year is a leap year. A normal year has 365 days, leap years have 366, with an extra day in February. 
#           The reason why we have leap years is really fascinating, this video does it more justice:

# This is how you work out whether if a particular year is a leap year.

# 🚨 Don't change the code below 👇
year = int(input("Which year do you want to check? "))
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

year_out_4 = year % 4
year_out_100 = year % 100
year_out_400 = year % 400

if year_out_4 == 0:
  if year_out_100 == 0:
    if year_out_400 == 0:
      print(f"The year {year}, is actually a leap year. :D ")
    else:
      print(f"The year {year}, is not a leap year. ")
  else:
    print(f"The year {year}, is not a leap year. ")
else:
  print(f"The year {year}, is not a leap year. ")
  