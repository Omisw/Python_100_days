# Day 8 - Function practice.


# Review: 
# Create a function called greet(). 
# Write 3 print statements inside the function.
# Call the greet() function and run your code.

#Simple Function
def greet():
  print("Hello Omar")
  print("How do you do Pepito Perez?")
  print("Isn't the weather nice today?")
greet()

#Function that allows for input
#'name' is the parameter.
#'Jack Bauer' is the argument.
def greet(name):
  print(f"Hello {name}")
  print(f"How are you today {name}?")
  print("!!")
greet("Omar")

#Functions with more than 1 input
def greet_with(name, location):
  print(f"Hello {name}")
  print(f"What is it like in {location}?")

#Calling greet_with() with Positional Arguments
greet_with("Omar Camacho", "Nowhere")
#vs.
greet_with("Nowhere", "Omar Camacho")


#Calling greet_with() with Keyword Arguments
greet_with(location="México", name="Omar Camacho")
