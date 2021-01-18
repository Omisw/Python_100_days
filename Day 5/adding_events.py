# Day 5 - Third exercise.

# Adding Evens

# Instructions
# You are going to write a program that calculates the sum of all the even numbers from 1 to 100, including 2 and 100.

# e.g. 2 + 4 + 6 + 8 +10 ... + 98 + 100

# Important, there should only be 1 print statement in your console output. It should just print the final total and not every step of the calculation.

#Write your code below this row 👇
sum_number = 0

for number in range(2, 101, 2):
  sum_number += number

print(f"The sum of all numbers is: {sum_number}")
