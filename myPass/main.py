import tkinter
from tkinter import *


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def gen_password():
    pass
# ---------------------------- SAVE PASSWORD ------------------------------- #
def save_password():
    pass
# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("myP4ss")
window.config(padx=40, pady=40)

canvas = Canvas(width=105, height=200)
lock_img = PhotoImage(file="logo.png")
canvas.create_image(52, 100, image=lock_img)
canvas.grid(column = 1, row = 0)
#Labels
web_label = Label(text="Website:")
web_label.grid(column=0, row=1)
Email_label = Label(text="Email/Username:")
Email_label.grid(column=0, row=2)
pass_label = Label(text="Password:")
pass_label.grid(column=0, row=3)
#Entries
web_entry = Entry(width=35)
web_entry.grid(column = 1, row = 1, columnspan = 2)
email_entry = Entry(width=35)
email_entry.grid(column = 1, row = 2, columnspan = 2)
pass_entry = Entry(width=16)
pass_entry.grid(column = 1, row = 3)
#Buttons
gen_pass = Button(text="Generate Password", command=gen_password)
gen_pass.grid(column = 2, row = 3)
add_profile = Button(text="Add",width=30, command=save_password)
add_profile.grid(column = 1, row = 4, columnspan = 2)

window.mainloop()