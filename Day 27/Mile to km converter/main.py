from tkinter import *

window = Tk()
window.minsize(width=150, height=100)
window.title("Mile to Km Converter")
window.config(padx=25, pady=25)

def converter():
    new_km = round(float(input_mile.get()) * 1.609, 2)
    label_km_converter.config(text=new_km)

label_mile = Label(text="Miles")
label_mile.grid(column=2, row=0)

label_km = Label(text="Km")
label_km.grid(column=2, row=1)

label_equal = Label(text="Is equal to")
label_equal.grid(column=0, row=1)

label_km_converter = Label(text="0")
label_km_converter.grid(column=1, row=1)

input_mile = Entry()
input_mile.grid(column=1, row=0)

converter_button = Button(text="Converter", command=converter)
converter_button.grid(column=1, row=2)


window.mainloop()