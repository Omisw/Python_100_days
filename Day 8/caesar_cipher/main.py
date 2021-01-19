from art import logo
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'ñ', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'ñ', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

print(logo)

def caesar(start_text, shift_amount, cipher_direction):
  end_text = ""
  if cipher_direction == "decode":
    shift_amount *= -1
  for char in start_text:
    if char in alphabet:
      position = alphabet.index(char)
      new_position = position + shift_amount
      end_text += alphabet[new_position]
    else:
      end_text += char
  print(f"Here's the {cipher_direction}d result: {end_text}")

def restart():
  still_trying = True
  while still_trying == True:
    go_again = input("Do you want try again?, type, Yes or No \n").lower()
    if go_again == "no":
      still_trying = False
      print("Goodbye")
    elif go_again == "yes":
      still_trying = True 
      direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
      text = input("Type your message:\n").lower()
      shift = int(input("Type the shift number:\n"))
      
    caesar(start_text=text, shift_amount=shift, cipher_direction=direction)

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

shift = shift % 27

caesar(start_text=text, shift_amount=shift, cipher_direction=direction)
restart()
