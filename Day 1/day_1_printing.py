# Day 1 - Start.

say_hi = "hello"
print(say_hi + " world!")

# Day 1 - First exercise.

print("Day 1 - String Manipulation")
print('String Concatenation is done with the " + " sign.')
print('e.g. print(" Hello " + " world ")')
print("New lines can be created with a backslash and n.")

# Day 1 - Second exercise.

print("The length of the name is " + str(len(input("What is your name? "))))

# Day 1 - Fourth exercise.

# Instructions
# Write a program that switches the values stored in the variables a and b.

# Warning. Do not change the code on lines 1-4 and 15-18. 
# Your program should work for different inputs. e.g. any value of a and b.

# 🚨 Don't change the code below 👇
a = input("a: ")
b = input("b: ")
# 🚨 Don't change the code above 👆

####################################
# Write your code below this line 👇

a, b = b, a

# Write your code above this line 👆
####################################

# 🚨 Don't change the code below 👇
print("a: " + a)
print("b: " + b)