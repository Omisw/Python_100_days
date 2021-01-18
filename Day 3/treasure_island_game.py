# Day 3 - Final challenge.


print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.") 

#https://www.draw.io/?lightbox=1&highlight=0000ff&edit=_blank&layers=1&nav=1&title=Treasure%20Island%20Conditional.drawio#Uhttps%3A%2F%2Fdrive.google.com%2Fuc%3Fid%3D1oDe4ehjWZipYRsVfeAx2HyB7LCQ8_Fvi%26export%3Ddownload
print('''*******************************************************************************''')
first_road = input("You're at a crossroad, where do you want to go, to 'right' or 'left'?: \n").lower()

if first_road == "left":
  second_road = input("You've come to a lake. There is a island in the middle of the lake, do you want to 'swim' across or 'wait' for a boat?: \n").lower()
  if second_road == "wait":
    third_road = input("You  arrive at the island unharmed. There is a house with 3 doors, one 'red', one 'yellow' and one 'blue'. Which color do you choose?: \n").lower()
    if third_road == "yellow":
      print('''
                *******************************************************************************
                        |                   |                  |                     |
                _________|________________.=""_;=.______________|_____________________|_______
                |                   |  ,-"_,=""     `"=.|                  |
                |___________________|__"=._o`"-._        `"=.______________|___________________
                        |                `"=._o`"=._      _`"=._                     |
                _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
                |                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
                |___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
                        |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
                _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
                |                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
                |___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
                ____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
                /______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
                ____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
                /______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
                ____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
                /______/______/______/______/______/______/______/______/______/______/_____ /
                *******************************************************************************
                Congrats you find the treasure! You win!!
            ''')
    elif third_road == "red":
      print("It's a room full of fire. Game over.")
    elif third_road == "blue":
      print("You enter a room of beasts. Game over.")
    else:
      print("You choose a door that doesn't exist. Game over.")
  else:
    print("You got attacked by an angry cocodrile")
else: 
  print("You fell into a hole!. Game over.")
  