# Day 3 - Second exercise.


# BMI Calculator 2.0

# Instructions

# Write a program that interprets the Body Mass Index (BMI) based on a user's weight and height.
# It should tell them the interpretation of their BMI based on the BMI value.
# Under 18.5 they are underweight
# Over 18.5 but below 25 they have a normal weight
# Over 25 but below 30 they are slightly overweight
# Over 30 but below 35 they are obese
# Above 35 they are clinically obese.
# The BMI is calculated by dividing a person's weight (in kg) by the square of their height (in m):
# Warning you should round the result to the nearest whole number. The interpretation message needs to include the words in bold from the interpretations above. 
#         e.g. underweight, normal weight, overweight, obese, clinically obese.

# 🚨 Don't change the code below 👇
height = float(input("enter your height in m: "))
weight = float(input("enter your weight in kg: "))
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

bmi_result = round(weight / height ** 2, 2)
print(bmi_result)
if bmi_result <= 18.5:
  print(f"Your BMI is {bmi_result}, you're underweight")
elif bmi_result <= 25:
  print(f"Your BMI is {bmi_result}, you're normalweight")
elif bmi_result <= 30:
  print(f"Your BMI is {bmi_result}, you're overweight")
elif bmi_result <= 35:
  print(f"Your BMI is {bmi_result}, you're obese")
else:
  print(f"Your BMI is {bmi_result}, you're clinically obese")
  