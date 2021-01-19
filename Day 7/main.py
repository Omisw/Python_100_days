import random
from hangman_words import word_list
from hangman_art import (stages, logo)

chosen_word = random.choice(word_list)
word_length = len(chosen_word)
end_of_game = False
lives = 6

print(logo)

#print(f'Pssst, the solution is {chosen_word}.')

display = []

for _ in range(word_length):
    display += "_"

while not end_of_game:
    guess = input("Guess a letter: ").lower()

    if guess in display:
      print(f"You already have type the letter {guess} before")
    elif guess in chosen_word:
      print(f"The letter {guess}, is in the word. ")
    else: 
      print(f"The letter {guess}, is not in the word, you lose a life. ")

    for position in range(word_length):
        letter = chosen_word[position]
        
        if letter == guess:
            display[position] = letter

    if guess not in chosen_word:
        lives -= 1
        if lives == 0:
            end_of_game = True
            print("You lose.")

    print(f"{' '.join(display)}")

    if "_" not in display:
        end_of_game = True
        print("You win.")

    print(stages[lives])