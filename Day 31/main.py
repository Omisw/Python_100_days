from tkinter import *
import pandas
import random

BACKGROUND_COLOR = "#B1DDC6"
new_word = {}
new_word_to_learn = {}

try:
    new_data = pandas.read_csv("data/words_to_learn.csv")
except FileNotFoundError:
    data = pandas.read_csv("data/french_words.csv")
    new_word_to_learn = data.to_dict(orient="records")
else:
    new_word_to_learn = new_data.to_dict(orient="records")


# ------------------- CHANGE WORD ------------------ #
def change_word():
    global new_word
    global timer_card
    window.after_cancel(timer_card)
    new_word = random.choice(new_word_to_learn)
    canvas.itemconfig(language_title, text="French", fill="black")
    canvas.itemconfig(french_word, text=new_word["French"], fill="black")
    canvas.itemconfig(new_image, image=card_front)
    timer_card = window.after(3000, change_card)


# ------------------- CHANGE CARD ------------------ #
def change_card():
    canvas.itemconfig(language_title, text="English", fill="white")
    canvas.itemconfig(french_word, text=new_word["English"], fill="white")
    canvas.itemconfig(new_image, image=card_back)


# ------------------- SAVE WORD ------------------ #
def save_word():
    new_word_to_learn.remove(new_word)
    words_data = pandas.DataFrame(new_word_to_learn)
    words_data.to_csv("data/words_to_learn.csv", index=False)
    change_word()


window = Tk()
window.title("Flashy")
window.config(bg=BACKGROUND_COLOR, padx=50, pady=50)
timer_card = window.after(3000, change_card)

# Images files
card_front = PhotoImage(file="images/card_front.png")
card_back = PhotoImage(file="images/card_back.png")
right = PhotoImage(file="images/right.png")
wrong = PhotoImage(file="images/wrong.png")

# Cards
canvas = Canvas(width=820, height=535, bg=BACKGROUND_COLOR, highlightthickness=0)
new_image = canvas.create_image(420, 265, image=card_front)

# Texts
language_title = canvas.create_text(420, 115, text="", font=("arial", 40, "italic"))
french_word = canvas.create_text(420, 260, text="", font=("arial", 60, "bold"))
canvas.grid(column=0, row=0, columnspan=2)

# Buttons
button_wrong = Button(image=wrong, highlightthickness=0, command=change_word)
button_wrong.grid(column=0, row=1)
button_right = Button(image=right, highlightthickness=0, command=save_word)
button_right.grid(column=1, row=1)

change_word()


window.mainloop()