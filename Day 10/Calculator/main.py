# Day 10 - Final challenge.


from art import logo
# from replit import clear

def add(number_1, number_2):
  return number_1 + number_2
def subtract(number_1, number_2):
  return number_1 - number_2
def multiply(number_1, number_2):
  return number_1 * number_2
def divide(number_1, number_2):
  return number_1 / number_2

operations = {
  "+": add, 
  "-": subtract, 
  "*": multiply,
  "/": divide
}

def calculator():
  print(logo)
  still_calc = True

  number_1 = float(input("Whats the firts number? "))

  for symbol in operations:
    print(symbol)

  while still_calc:
    operator_sym = input("Pick an operation: ")
    number_2 = float(input("Whats the next number? "))
    result = operations[operator_sym](number_1, number_2)

    if operator_sym == "+":
      print(f"{number_1} {operator_sym} {number_2} = {result}")
    elif operator_sym == "-":
      print(f"{number_1} {operator_sym} {number_2} = {result}")
    elif operator_sym == "*":
      print(f"{number_1} {operator_sym} {number_2} = {result}")
    elif operator_sym == "/":
      print(f"{number_1} {operator_sym} {number_2} = {result}")

    continue_calc = input(f"Type 'y' to continue calculating with {result}, or type 'n' to start a new calculating ")
    
    if continue_calc == "y":
      number_1 = result
      still_calc = True
    #   clear()
    elif continue_calc == "n":
      still_calc = False
    #   clear()
      calculator()

calculator()
