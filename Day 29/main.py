from tkinter import *
from tkinter import messagebox
from random import choice, randint, shuffle
import pyperclip
# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def password_generator():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
               'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    ran_letters = [choice(letters).strip(" ") for char in range(randint(8, 10))]
    ran_symbols = [choice(symbols).strip(" ") for char in range(randint(2, 4))]
    ran_numbers = [choice(numbers).strip(" ") for char in range(randint(2, 4))]
    password_list = ran_letters + ran_symbols + ran_numbers
    shuffle(password_list)
    password = "".join(password_list)

    pass_entry.insert(0, password)
    pyperclip.copy(password)
# ---------------------------- SAVE PASSWORD ------------------------------- #
def save_password():
    password_file = open("password_manager.txt", "a")
    website = website_entry.get()
    email = email_entry.get()
    password = pass_entry.get()

    if website == "" or email == "" or password == "":
        messagebox.showinfo(title="Empty fields", message="Please don't left empty fields!")

    if website != "" and email != "" and password != "":
        is_ok = messagebox.askokcancel(title="Confirm account", message=f"These are the details entered: \nWebsite: {website}\n"
                                                                f"Email: {email}\nPassword: {password}\nIs it ok to save?")

    if is_ok:
        password_file.write(f"{website} | {email} | {password} \n")
        website_entry.delete(0, END)
        pass_entry.delete(0, END)

# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Password manager")
window.config(padx=35, pady=35)


canvas = Canvas(width=200, height=200)
logo = PhotoImage(file="logo.png")
canvas.create_image(100, 120, image=logo)
canvas.grid(column=1, row=0)

# Labels
website_label = Label(text="Website:")
website_label.grid(column=0, row=1)
email_label = Label(text="Email/Username:")
email_label.grid(column=0, row=2)
pass_label = Label(text="Password:")
pass_label.grid(column=0, row=3)

# Entries
website_entry = Entry(width=52)
website_entry.grid(column=1, row=1, columnspan=2)
website_entry.focus()
email_entry = Entry(width=52)
email_entry.grid(column=1, row=2, columnspan=2)
email_entry.insert(0, 'ejemplo@correo.com')
pass_entry = Entry(width=33)
pass_entry.grid(column=1, row=3)

# Buttons
pass_generate = Button(text="Generate Password", command=password_generator)
pass_generate.grid(column=2, row=3)
add_pass = Button(text="Add", width=44, command=save_password)
add_pass.grid(column=1, row=4, columnspan=2)


window.mainloop()