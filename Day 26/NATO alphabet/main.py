import pandas

# TODO 1. Create a dictionary in this format:

# {"A": "Alfa", "B": "Bravo"}
nato_alphabet = pandas.read_csv("nato_phonetic_alphabet.csv")

nato_alphabet_dictionary = {row.letter: row.code for (index, row) in nato_alphabet.iterrows()}
print(nato_alphabet_dictionary)

#TODO 2. Create a list of the phonetic code words from a word that the user inputs.

user_word = input("Give me a phrase: ").upper()
phonetic_words = [nato_alphabet_dictionary[letter] for letter in user_word]
print(phonetic_words)
