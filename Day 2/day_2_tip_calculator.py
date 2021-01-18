#If the bill was $150.00, split between 5 people, with 12% tip. 
#Each person should pay (150.00 / 5) * 1.12 = 33.6
#Format the result to 2 decimal places = 33.60
#Tip: You might need to do some research in Google to figure out how to do this.

print("Welcome to the tip calculator")

total_bill = float(input("What was the total bill? "))
porcentage_tip = input("What porcentage tip would you like to give? 10, 12 or 15? ")
total_split = float(input("How many people to split the bill? "))

final_tip = float(f"1.{porcentage_tip}")
print(final_tip)
final_bill = round(total_bill * final_tip / total_split, 2)

messege = f"Each person should pay: ${final_bill}"
print(messege)
